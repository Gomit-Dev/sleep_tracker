# Sleep Tracker Backend

This is the backend service for the Sleep Tracker application. It provides APIs and functionality to manage user data, sleep records, and analytics.

## Features

- User authentication and authorization
- CRUD operations for sleep records
- Data analytics for sleep patterns
- RESTful API design

## Technologies Used

- **Programming Language**: Python
- **Framework**: Flask
- **Database**: MongoDB
- **Authentication**: JSON Web Tokens (JWT)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/sleep-tracker-backend.git
    cd sleep-tracker-backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add the following:
    ```
    PORT=3000
    MONGO_URI=your_mongodb_connection_string
    JWT_SECRET=your_jwt_secret
    ```

5. Start the server:
    ```bash
    flask run
    ```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login a user

### Sleep Records
- `GET /api/sleep` - Get all sleep records
- `POST /api/sleep` - Add a new sleep record
- `PUT /api/sleep/:id` - Update a sleep record
- `DELETE /api/sleep/:id` - Delete a sleep record

### Analytics
- `GET /api/analytics` - Get sleep pattern analytics

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [gomit.dev@example.com].

