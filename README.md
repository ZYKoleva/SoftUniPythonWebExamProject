# Real Estate Website for viewing and posting real estate ads. 
Web application is built with Django and is using Postgresql for storing data. Bootstrap and custom CSS used.
The application consists of users, adds for real estate, static page about us and general rules. 
Users can register, login and logout. Unregistered users can view ads, filter ads by different criteria and sort the results based on modified date, price and most viewed.
Registered users can view all ads, can create, edit and delete their own adds.
Admin users can create, edit, delete, approve reject and leave reason for rejection for all ads as well as create and delete users

 

### Structure
    /estate_app
    /estate_app_auth
    /media
        // images
    /static
        //img
        //javascript
        //style
    /templates
        //common
        //filter_section
        pages
    
    
### Functionality
    **Users**
        o Register
        o Login
        o Logout
    **Ads**
        o Unregistered 
            View All Ads
            View Filtered Ads based on criteria: location, type, sale or rent
            Sort Ads based on price, newest, most viewed
            View Ad's details
        o Registered Users
            All functionalities as unregistered users
            Create own ads
            Filter by own ads
            View ad's details and their status, if pending approval or is rejected
            Edit thier own ads
        
        o Admin users
            All functionalities as registered users
            Approve ads
            Reject ads
            View pending for approval ads
            
            

   
        
    
