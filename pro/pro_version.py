# def translate_text(text, lang):
#     """Translate a given text to a specified language."""
#     try:
#         # Split the text into chunks of no more than 5000 characters
#         text_chunks = []
#         while len(text) > 0:
#             if len(text) > 5000:
#                 split_index = text[:5000].rfind(" ")
#                 text_chunks.append(text[:split_index])
#                 text = text[split_index:]
#             else:
#                 text_chunks.append(text)
#                 text = ""

#         translated_text_chunks = []
#         for chunk in text_chunks:
#             with st.spinner(LANGUAGES[lang]['language']):
#                 translated_chunk = GoogleTranslator(source='auto', target=lang).translate(chunk)
#                 translated_text_chunks.append(translated_chunk)
        
#         # Combine all translated chunks
#         translated_text = ' '.join(translated_text_chunks)

#         return translated_text
#     except Exception as e:
#         logging.error(f'Error during translation: {e}')
#         return None