import pika
import json
from fpdf import FPDF
import uuid
import os

def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Student Information", ln=True, align="C")
    pdf.ln(10)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key.capitalize()}: {value}", ln=True)


    folder_path = os.path.join(os.getcwd(), 'media', 'pdfs')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"report_{uuid.uuid4()}.pdf"
    filepath = os.path.join(folder_path, filename)
    pdf.output(filepath)
    print(f"✅ PDF saved to: {filepath}")


    
def callback(ch, method, properties, body):
    data = json.loads(body.decode())
    print("📩 Received message:", data)
    generate_pdf(data)

params = pika.URLParameters('amqps://poaxryvt:XcOKhmp9oiEG9n_huXHnqXvg2lJzLNHJ@puffin.rmq2.cloudamqp.com/poaxryvt')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="my_queue")
channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)

print("👂 Consumer waiting for PDF tasks...")
channel.start_consuming()
