# AI Resume Generator

A modern web application that generates professional resumes using Google's Gemini AI based on job titles. The application is built with Python Flask and containerized using Docker.

## Features

- Generate professional resumes based on job titles
- Modern, responsive UI using Tailwind CSS
- PDF download functionality
- Dockerized environment for easy deployment
- Powered by Google's Gemini AI

## Prerequisites

- Docker and Docker Compose installed on your system
- Google Gemini API key

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd resumebuilder
```

2. Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

3. Using Docker Compose (Recommended):
```bash
docker-compose up -d
```

OR using Docker directly:
```bash
docker build -t resume-generator .
docker run -p 5000:5000 --env-file .env resume-generator
```

The application will be available at `http://localhost:5000`

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter a job title (e.g., "DevOps Engineer", "Python Developer", "Network Engineer")
3. Click "Generate Resume" or press Enter
4. View the generated resume
5. Click "Download PDF" to save the resume as a PDF file

## Docker Commands

### Using Docker Compose
- Start the application: `docker-compose up -d`
- Stop the application: `docker-compose down`
- View logs: `docker-compose logs -f`
- Rebuild and start: `docker-compose up -d --build`

### Using Docker directly
- Build the image: `docker build -t resume-generator .`
- Run the container: `docker run -p 5000:5000 --env-file .env resume-generator`
- Stop the container: `docker stop resume-generator`
- View logs: `docker logs -f resume-generator`

## Development

To run the application locally without Docker:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Security Notes

- Never commit your `.env` file or expose your API key
- The application runs as a non-root user in the Docker container
- All API calls are made server-side to protect your API key
- Docker Compose includes health checks to ensure service availability

## License

MIT License 