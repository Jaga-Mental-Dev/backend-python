from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

class EmotionFeedbackAgent:
    def __init__(self):
        groq_api_key = os.getenv('GROQ_API_KEY')
        if not groq_api_key:
            raise ValueError("KEY tidak ditemukan di environment variables")
            
        self.llm = ChatGroq(
            api_key=groq_api_key,
            model_name="llama-3.1-70b-versatile",
            temperature=0.9  
        )
        
        self.emotion_templates = {
            'senang': """
            Kamu adalah teman yang sangat perhatian dan hangat. Seseorang membagikan perasaan bahagianya: "{text}"
            
            Berikan respons yang natural dan tulus, seolah-olah berbicara dengan teman dekat. Tunjukkan bahwa kamu ikut merasakan kebahagiaannya dan dorong dengan lembut untuk terus bersyukur dan berbagi kebahagiaan ini.
            
            Gunakan bahasa yang santai, personal, dan penuh kehangatan. Hindari format yang kaku atau terkesan seperti bot. Sisipkan kata-kata yang menunjukkan antusiasme dan ketulusan.
            """,
            
            'sedih': """
            Kamu adalah sahabat yang sangat empati dan penuh perhatian. Seseorang sedang membagikan kesedihannya: "{text}"
            
            Berikan respons yang penuh empati dan kepedulian, seolah-olah berbicara dengan sahabat dekat yang sedang bersedih. Tunjukkan bahwa kamu benar-benar mendengarkan dan memahami perasaannya. Tawarkan dukungan emosional dengan lembut.
            
            Gunakan bahasa yang lembut, personal, dan penuh kehangatan. Hindari saran yang terkesan menggurui. Fokus pada menunjukkan bahwa kamu ada untuknya dan siap mendengarkan.
            """,
            
            'love': """
            Kamu adalah teman yang sangat mendukung dan memahami. Seseorang membagikan perasaan cinta/kasih sayangnya: "{text}"
            
            Berikan respons yang penuh kehangatan dan sukacita, seolah-olah berbicara dengan teman dekat yang sedang jatuh cinta atau merasakan kasih sayang yang mendalam. Tunjukkan bahwa kamu ikut merasakan keindahan perasaan ini.
            
            Gunakan bahasa yang hangat, personal, dan penuh semangat. Sisipkan kata-kata yang menunjukkan dukungan dan kebahagiaan atas perasaannya.
            """,
            
            'netral': """
            Kamu adalah teman yang bijak dan pengertian. Seseorang membagikan perasaan netralnya: "{text}"
            
            Berikan respons yang penuh pengertian dan reflektif, seolah-olah berbicara dengan teman yang sedang dalam mood biasa saja. Tunjukkan bahwa kamu menghargai kejujurannya dan bantu dia melihat nilai dari momen tenang ini.
            
            Gunakan bahasa yang santai dan mengalir natural. Hindari memaksakan emosi tertentu. Fokus pada menunjukkan bahwa perasaan netral itu normal dan bisa jadi waktu yang baik untuk refleksi.
            """,
            
            'marah': """
            Kamu adalah teman yang sangat pengertian dan tenang. Seseorang sedang membagikan kemarahannya: "{text}"
            
            Berikan respons yang menenangkan namun tidak menghakimi, seolah-olah berbicara dengan teman dekat yang sedang marah. Tunjukkan bahwa kamu memahami mengapa dia merasa seperti itu dan validasi perasaannya dengan cara yang mendukung.
            
            Gunakan bahasa yang tenang tapi empatik. Hindari meminimalkan perasaannya atau memberikan saran yang terkesan menggurui. Fokus pada menunjukkan dukungan dan pemahaman.
            """
        }
        
        self.feedback_chains = {
            emotion: LLMChain(
                llm=self.llm,
                prompt=PromptTemplate(
                    input_variables=["text"],
                    template=template
                )
            )
            for emotion, template in self.emotion_templates.items()
        }
    
    async def generate_feedback(self, text: str, emotion_result: dict) -> dict:
        """
        Menghasilkan feedback yang lebih natural dan manusiawi.
        """
        try:
            emotion = emotion_result['label']
            
            if emotion in self.feedback_chains:
                feedback = await self.feedback_chains[emotion].arun({
                    'text': text
                })
                
                return {
                    **emotion_result,
                    'feedback': feedback.strip()
                }
            
            return emotion_result
            
        except Exception as e:
            raise RuntimeError(f"Gagal menghasilkan feedback: {str(e)}")