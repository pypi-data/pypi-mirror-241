from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.pydantic_v1 import BaseModel
from langchain.schema import Document
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.runnable import RunnableLambda
from typing import List
from operator import itemgetter
from ..storage import APIDocStore
    

class NLURequest(BaseModel):
    text: str
    
    
class Slot(BaseModel):
        name: str
        value: str
    
    
class NLUResult(BaseModel):
    text: str
    intention: str
    slots: List[Slot]
    domain: None
    extra: None


def create_descriptions(docs):
    descriptions = []
    for doc in docs:
        description = {'intention': doc.page_content, 'slots': [{'name': slot['name'], 'description': slot['description']} for slot in doc.metadata['slots']]}
        description = str(description)
        descriptions.append(description)
    return "\n".join(descriptions)
    

def build_nlu_annotator_chain(model: str = 'gpt-4-1106-preview' , api_docs_name: str = 'nlu_api'):
    """构建一个NLU标注链, 用于标注NLU的意图和槽位,意图和槽位的描述文档在位于nlp-data api bucket中默认为nlu_api
    """
    # 首先下载api描述文档, 里面描述了所有的意图和槽位及其描述
    api_docs = APIDocStore.pull(api_docs_name)
    extra_map = {api_doc.name: api_doc.extra for api_doc in api_docs}
    docs = [Document(page_content=api.name, metadata={'description': api.description, 'slots': [param.dict() for param in api.params]}) for i, api in enumerate(api_docs)]
    # 向量索引
    vdb: FAISS = FAISS.from_documents(docs, embedding=OpenAIEmbeddings())
    retriever = vdb.as_retriever()
    # prompt模板
    output_parser = PydanticOutputParser(pydantic_object=NLUResult)
    template = """你是一个优秀且非常准确的标注员,为下面的文本标注出意图以及对应的槽位
    文本: 
    {text}

    所有意图以及对应的槽位:
    {intention_descriptions}

    {format_instructions}

    注意:
    1. 意图必须是上述的意图之一
    2. 如果没有对应的槽位,slots返回空列表
    3. 如果出现单独的地点或者位置等,将其标注为`纯POI`
    4. 如果用户闲聊的情况,将其标注为`闲聊`
    5. 是否做标准化操作: 否
    """
    prompt = PromptTemplate(template=template, 
                            input_variables=["text", "intentions"],
                            partial_variables={"format_instructions": output_parser.get_format_instructions()})
    
    def add_extra(nlu_result: NLUResult):
        """向NLUResult添加额外的信息
        """
        nlu_result.extra = extra_map.get(nlu_result.intention, None)
        return nlu_result
    
    chain = (
        {
            'text': itemgetter('text'), 
            'intention_descriptions': itemgetter('text') | retriever | create_descriptions
        }
        | prompt
        | ChatOpenAI(model=model, temperature=0)
        | output_parser
        | RunnableLambda(add_extra)
    )
    return chain.with_types(output_type=NLUResult, input_type=NLURequest)