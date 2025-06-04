import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY found in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_resume(job_title, followup_keywords=None):
    prompt = f"""
You are a professional resume writer. Create a highly polished, modern, and ATS-friendly resume for a {job_title} position. Use a clean, professional HTML structure (no markdown, no code blocks). The resume should include:

- Name and contact info (use realistic placeholders)
- Professional Summary (2-3 sentences, impactful)
- Key Skills (bullet points, grouped if possible)
- Work Experience (3-4 relevant positions, each with job title, company, years, and 2-4 bullet points of achievements)
- Education (degree, institution, year)
- Certifications (if applicable)

Use strong, action-oriented language. Make the layout visually appealing and easy to read. Use <h2> for section headers, <ul>/<li> for lists, and <strong> for highlights. Do NOT use markdown or code blocks. Do NOT include triple backticks. Only return valid HTML for the resume content.
"""
    if followup_keywords:
        prompt += f"\n\nAdditional customization instructions: {followup_keywords}"
    try:
        response = model.generate_content(prompt)
        html = response.text
        # Remove any accidental markdown/code block formatting
        html = html.replace('```html', '').replace('```', '').strip()
        return html
    except Exception as e:
        return f"Error generating resume: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    job_title = data.get('job_title', '').strip()
    followup_keywords = data.get('followup_keywords', '').strip()
    if not job_title:
        return jsonify({'error': 'Job title is required'}), 400
    resume_content = generate_resume(job_title, followup_keywords)
    return jsonify({'resume': resume_content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 