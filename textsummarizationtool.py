pip install transformers torch
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
The College Management System is a web-based application developed to streamline and integrate all aspects of college operations. 
It allows students to register for courses, check their attendance, receive academic updates, and pay fees in one platform. 
Faculty can upload materials, manage assignments, and track student progress. 
The system sends real-time notifications for deadlines, announcements, and events, ensuring all stakeholders are aligned.
"""

summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
print("Summary:\n", summary[0]['summary_text'])
