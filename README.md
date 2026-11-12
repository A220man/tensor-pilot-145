# Tensor-Pilot-145

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


## Overview
Tensor-Pilot-145 is a **Universal SEO skill for Claude Code** providing comprehensive data fetching and analysis capabilities. This repository contains the core implementation for SEO data retrieval, keyword analysis, and SERP fetching functionality.

## Features
- Keyword analysis with search volume, difficulty scores, and CPC
- SERP data fetching with domain authority and page rank
- Advanced caching for performance optimization
- Real-time monitoring and statistics

## API Endpoints

### GET /
**Description:** API information and capabilities overview

### POST /api/seo/keyword/analyze
**Description:** Analyze keyword and fetch SERP data

**Request Body:**
```json
{
  "keyword": "string (required)",
  "location": "US (optional)",
  "language": "en (optional)",
  "limit": 10 (optional)
}
```

**Response:**
```json
{
  "keyword": "string",
  "search_volume": 1000,
  "difficulty_score": 50,
  "cpc": 0.5,
  "serp_results": [...],
  "timestamp": "2024-01-01T00:00:00Z",
  "cache_key": "string"
}
```

### GET /api/seo/keyword/{keyword}
**Description:** Get cached keyword analysis

### GET /api/seo/cache/stats
**Description:** Get cache statistics

### GET /api/seo/health
**Description:** Health check endpoint

## Installation

### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

### Installation Steps
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
python main.py
```

Or with uvicorn for production:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Usage Examples

### Basic Keyword Analysis
```python
import requests

# Analyze a keyword
response = requests.post('http://localhost:8000/api/seo/keyword/analyze', json={
    'keyword': 'SEO optimization',
    'location': 'US',
    'language': 'en',
    'limit': 10
})

data = response.json()
print(f"Search Volume: {data['search_volume']}")
print(f"Difficulty Score: {data['difficulty_score']}")
```

### Get Cache Statistics
```python
response = requests.get('http://localhost:8000/api/seo/cache/stats')
stats = response.json()
print(f"Active Cache Entries: {stats['active_entries']}")
```

## Technical Specifications

### Framework
- **Backend:** FastAPI
- **Web Server:** Uvicorn
- **Language:** Python 3.7+
- **Dependencies:** Pydantic, python-multipart

### API Design
- RESTful architecture
- JSON responses
- Comprehensive error handling
- Request/response validation

### Performance Features
- Advanced caching system
- Background cleanup tasks
- Memory-efficient data structures
- Connection pooling

## Development

### Project Structure
```
tensor-pilot-145/
├── src/tensor-pilot-145/
│   └── api/
│       └── seo_data.py          # Core API implementation
├── main.py                      # FastAPI application
├── web-interface.html           # Web interface for testing
├── requirements.txt             # Dependencies
├── feature-plan.json            # Feature roadmap
├── PLAN.md                      # Implementation plan
└── README.md                    # This file
```

### Testing
Run tests with:
```bash
pytest
```

### Monitoring
- Health check endpoint available at `/health`
- Cache statistics at `/api/seo/cache/stats`
- Real-time monitoring capabilities

## Configuration

### Environment Variables
```bash
# Server configuration
UVICORN_HOST=0.0.0.0
UVICORN_PORT=8000
```

### Cache Settings
- TTL: 300 seconds (5 minutes)
- Memory-based caching
- Automatic cleanup of expired entries

## Security

### Authentication
- No authentication required (open API)
- Consider implementing authentication for production use

### Rate Limiting
- Basic rate limiting implemented
- Cache-based request throttling

## Production Considerations

### Deployment
- Use Gunicorn with Uvicorn workers
- Configure reverse proxy (nginx)
- Set up monitoring and logging
- Implement proper error handling

### Monitoring
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/seo/cache/stats
```

## Support

### Documentation
- This README for basic usage
- API endpoints documented above
- Web interface for interactive testing

### Community
- **GitHub Issues:** Report bugs or request features
- **Stack Overflow:** API usage questions
- **Documentation:** Comprehensive API docs

### Contact

For specific technical issues or custom development:
- **Email:** ryandtvo@gmail.com
- **Project:** Tensor-Pilot-145
- **Support:** Business hours (UTC timezone)

---

*This README provides comprehensive documentation for the Tensor-Pilot-145 SEO API. For additional information or specific questions, please refer to the project documentation or contact the development team.*