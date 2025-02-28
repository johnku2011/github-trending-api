# GitHub Trending API

A FastAPI-based REST API that scrapes and serves GitHub's trending repositories information. This API allows you to fetch trending repositories with various time frames (daily, weekly, monthly) and includes detailed repository information such as stars, forks, and descriptions.

## Motivation
Building this as current Github API doesn't have the trending repo data, have searchde online for online sources but the data format isn't what I want.
Please feel free to use and enhance the API.

Implemented the API in a Coze Bot: https://www.coze.com/store/agent/7476082421604155409

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
