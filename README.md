# Hack505 Dashboard

A modern, interactive hackathon information dashboard built with Flask, featuring dark mode, responsive design, and real-time event management.

## Features

- 🎯 **Interactive Event Schedule** - Real-time workshop and event listings
- 📢 **Clickable Announcements** - Detailed popups with full descriptions
- 🌙 **Dark/Light Mode Toggle** - Enhanced user experience with theme persistence
- 📱 **QR Code Sharing** - Easy mobile access to the dashboard
- 📱 **Mobile-Responsive Design** - Works perfectly on all devices
- ❓ **Question Submission System** - Direct mentor contact functionality
- ✨ **Modern UI/UX** - Glass morphism effects and smooth animations

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Responsive Grid Layout, CSS Animations
- **APIs**: REST endpoints for events and announcements
- **UI Libraries**: QR Code generation, Modern CSS features

## Project Structure

```
hack404Website/
├── app.py                 # Flask backend application
├── templates/
│   ├── dashboard.html     # Main dashboard template
│   └── ask_question.html  # Question submission form
├── static/               # CSS, JS, and other static files
└── README.md            # Project documentation
```

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ThatMasterCoder/hack404Website.git
   cd hack404Website
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:8000
   ```

## API Endpoints

- `GET /` - Main dashboard
- `GET /dashboard` - Dashboard page
- `GET /events` - JSON list of events
- `GET /announcements` - JSON list of announcements
- `GET/POST /ask_question` - Question submission form

## Features in Detail

### Interactive Dashboard
- **Event Schedule**: Live workshop listings with times and locations
- **Announcements**: Important hackathon updates with detailed descriptions
- **Hackathon Info**: About Hack505, cost information, and contact details

### User Experience
- **Dark Mode**: Toggle between light and dark themes with persistence
- **Mobile-First**: Responsive design that works on all screen sizes
- **Interactive Elements**: Hover effects, smooth transitions, and animations
- **Accessibility**: Keyboard navigation and screen reader support

### Technical Implementation
- **Flask Backend**: Clean REST API with structured data models
- **Modern Frontend**: CSS Grid, Flexbox, and modern JavaScript features
- **Glass Morphism**: Beautiful backdrop blur effects and transparency
- **Local Storage**: User preferences saved across sessions

## About Hack505

Hack505 is a 36-hour hackathon in Toronto, ON, bringing together 200 students passionate about learning and building projects that excite them. The event focuses on three core pillars: **education**, **innovation**, and **community**.

## Development Story

This project was built during Hack505 to solve the common problem of scattered hackathon information. The dashboard serves as a centralized hub where participants can easily access schedules, announcements, and important event details without hunting through multiple platforms.

### What We Learned
- Full-stack web development with Flask
- Modern CSS techniques and responsive design
- JavaScript DOM manipulation and event handling
- User experience design principles
- API design and data structure organization

### Challenges Overcome
- Implementing smooth dark mode transitions
- Creating responsive layouts for all devices
- Building interactive modal components
- Ensuring cross-browser compatibility

## Future Enhancements

- 🔄 Real-time updates with WebSockets
- 🔐 User authentication and personalization
- 📱 Push notifications for announcements
- 🎮 Integration with Discord/Slack
- 📊 Analytics dashboard for organizers
- 🌍 Multi-language support

## Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.

---

**Built with ❤️ during Hack505 in Toronto, ON**

*Bringing together students passionate about learning, innovation, and community.*
