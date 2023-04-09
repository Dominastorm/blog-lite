# Search
- [x] Get search results from the database
- [x] Add followed field to search results

# FollowToggle
- [x] Pass the userId to followToggle
- [x] Create API in flask for follow requests
- [x] Create API in flask for unfollow requests
- [x] Call API from FollowToggle
- [x] Update FollowToggle in FollowersView
- [x] Add FollowToggle to FollowingView
- [x] Add FollowToggle to SearchView

# Login/Logout
- [x] Add remember me functionality
- [x] Implement logout

# Profile
- [x] Make profiles unique for users (add :id to index.js)
- [x] Get accurate total posts count, followers count, following count

# CreatePostView
- [x] Make API function to create a post
- [x] Connect API with Vue
- [ ] Open the post once created

# Create pages/components
- [ ] PostList
- [ ] PostView
- [ ] Feed
- [ ] Insert PostList into feed
- [ ] Insert PostList into profile

# Posts
- [ ] Show blogs on feed based on timestamp (filter by users followed)
- [ ] Make sure blog content supports UTF-8 characters
- [ ] Abstract out the PostList component
- [ ] Add the PostList component to the Profile 
- [ ] Add author and date to posts
- [ ] Make feeds unique for users
- [ ] Edit Post functionality  
- [ ] Delete Post functionality
- [ ] Export Blog functionality
- [ ] Let blog content handle HTML tag

# Important
- [ ] Add Redis
- [ ] Add Celery
- [ ] Add page protection
- [ ] If users try to access any page without logging in, redirect them to login page

# Jobs
- [ ] Backend Jobs
- [ ] Export Jobs
- [ ] Reporting Jobs
- [ ] Alert Jobs

# Requests
- [ ] Add a request to get the user's feed
- [ ] Add a request to get the user's profile
- [ ] Add a request to get the user's followers
- [ ] Add a request to get the user's following
- [ ] Add a request to get the user's posts

# Miscellaneous
- [ ] Make the follow/unfollow button a component of its own
- [ ] Restyle the top part of profile
- [x] Change colour of "Choose file" in CreatePostView
- [ ] Add type hints to all functions
- [ ] Remove unused imports
- [ ] Remove unnecessary print statements
- [ ] Make styling global
- [ ] Use token for authentication
- [ ] Archive blogs
- [ ] Add option to upload images
