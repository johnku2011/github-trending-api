# GitHub Trending API

A FastAPI-based REST API that scrapes and serves GitHub's trending repositories information. This API allows you to fetch trending repositories with various time frames (daily, weekly, monthly) and includes detailed repository information such as stars, forks, and descriptions.

## Features

- 🚀 Fast and lightweight API
- 📊 Real-time GitHub trending repository data
- ⏱️ Multiple time frame options (daily/weekly/monthly)
- 🔄 CORS enabled for frontend integration
- 📝 Comprehensive repository information including:
  - Repository name
  - Direct GitHub link
  - Programming language
  - Star count
  - Fork count
  - Description
  - Stars gained in the period

## API Endpoints

### Get Trending Repositories

http 
GET /api/trending?time_frame={time_frame}


| Parameter    | Type   | Description                              |
|-------------|--------|------------------------------------------|
| time_frame  | string | Optional. Values: daily, weekly, monthly (default: daily) |

#### Response Format
json
{
"status": "success",
"data": [
{
"repo_name": "repository-name",
"link": "https://github.com/owner/repository-name",
"language": "Python",
"stars": 1000,
"forks": 100,
"description": "Repository description",
"stars_in_period": 50
}
]
}

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Node.js (for Vercel CLI)

### Installation

1. Clone the repository:
bash
git clone <your-repository-url>
cd github-trending-api


2. Create and activate a virtual environment:
bash
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate

3. Install dependencies:
bash
pip install -r requirements.txt


### Local Development

Run the development server:
bash
uvicorn api.index:app --reload


The API will be available at:
- Main API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc

### Project Structure

├── api/
│ ├── init.py
│ ├── index.py # FastAPI application
│ └── github_trending.py # Core scraping functionality
├── .gitignore
├── README.md
├── requirements.txt
└── vercel.json # Vercel deployment configuration

## Deployment

This project is configured for deployment on Vercel.

1. Install Vercel CLI:
bash
npm i -g vercel

2. Deploy to Vercel:
bash
vercel

3. For production deployment:
bash
vercel --prod

## Error Handling

The API returns appropriate HTTP status codes:

- `200`: Successful request
- `400`: Invalid time_frame parameter
- `500`: Server error (e.g., GitHub scraping failed)

## Rate Limiting

Please note that this API scrapes GitHub's trending pages. Implement appropriate rate limiting in your applications to avoid overwhelming GitHub's servers.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not affiliated with GitHub. It scrapes publicly available data from GitHub's trending pages. Please use responsibly and in accordance with GitHub's terms of service.

## Support

If you found this project helpful, please give it a ⭐️!