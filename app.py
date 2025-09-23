import boto3
import streamlit as st
import json
import uuid

# Initialize Bedrock client
bedrock_runtime = boto3.client('bedrock-runtime', region_name ='us-east-1')
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

# Set up the Streamlit interface
st.title("Knowledge Base Chatbot")
st.write("Ask me anything about the content from our websites!")

# Initialize chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.session_id = str(uuid.uuid4())

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Replace with your actual knowledge base ID
        knowledge_base_id = "AXCDSUBJLI"
        
        try:
            # Query the knowledge base
            response = bedrock_agent_runtime.retrieve_and_generate(
                input={
                    'text': prompt
                },
                retrieveAndGenerateConfiguration={
                    'knowledgeBaseConfiguration': {
                        'knowledgeBaseId': knowledge_base_id,
                        'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2'
                    }
                },
                sessionId=st.session_state.session_id
            )
            
            # Extract the response
            answer = response['output']['text']
            
            # Display the response
            message_placeholder.markdown(answer)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
        except Exception as e:

            message_placeholder.error(f"Error: {str(e)}")
