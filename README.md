**Vibezz**
==========

Vibezz is a modern music streaming and discovery platform built with Vue.js. It allows users to explore new music, create playlists, and interact with a vibrant music community.

**Table of Contents**
---------------------

*   Installation
   
   *   Backend Setup
       
   *   Frontend Setup
       
   *   Email Testing
       
*   Usage
   
*   Technologies Used
   
*   License
   

**Installation**
----------------

Before running the application, make sure you have the following dependencies installed:

*   Python 3.10 or higher
   
*   Node.js and npm
   
*   Celery
   
*   Flask
   
*   MailHog
   

### **Backend Setup**

1.  **Install Python dependencies**:
   
   ```
   pip install -r requirements.txt
   ```
   
2.  **Run Flask server**:
   
   ```
   flask run
   ```
   
3.  **Start Celery worker**:
   
   ```
   celery -A app.celery worker -l info
   ```
   
4.  **Start Celery beat for periodic tasks**:
   
   ```
   celery -A app.celery beat -max-interval 2 -l info
   ```
   

### **Frontend Setup**

1.  **Navigate to the 'frontend' folder**:
   
   ```
   cd frontend
   ```
   
2.  **Install Node.js dependencies**:
   
   ```
   npm install
   ```
   
3.  **Run the Vue.js development server**:
   
   ```
   npm run serve
   ```
   

### **Email Testing**

To test emails during development, you can use MailHog. Make sure MailHog is installed and running:

    ~/go/bin/MailHog


**Usage**
---------

Vibezz is a music streaming and discovery platform. Users can:

1.  Browse and discover new music
    
2.  Create personalized playlists
    
3.  Follow artists and other users
    
4.  Interact with the music community through comments and likes
    

To get started, simply run the backend and frontend setup as described above, and navigate to `http://localhost:8080` in your web browser.

**Technologies Used**
---------------------

*   **Backend**:
    
    *   Python
        
    *   Flask
        
    *   SQLAlchemy
        
    *   Celery
        
*   **Frontend**:
    
    *   Vue.js
        
    *   Vuex
        
    *   Vue Router
        
    *   Axios
        
*   **Deployment**:
    
    *   Docker
        
    *   Nginx
        

**License**
-----------

Vibezz is released under the MIT License.
