// PRACTICAL 6 - Instagram-like database using MongoDB (run inside mongosh)

use instagram_db


db.users.insertMany([
  { user_id: 1, username: "simran", name: "Simran Kaur", email: "simran@gmail.com", followers: 1200, following: 350 },
  { user_id: 2, username: "aman", name: "Aman Singh", email: "aman@gmail.com", followers: 850, following: 420 },
  { user_id: 3, username: "priya", name: "Priya Sharma", email: "priya@gmail.com", followers: 2100, following: 500 },
  { user_id: 4, username: "rahul", name: "Rahul Kumar", email: "rahul@gmail.com", followers: 650, following: 300 },
  { user_id: 5, username: "neha", name: "Neha Verma", email: "neha@gmail.com", followers: 1800, following: 450 }
])


db.posts.insertMany([
  { post_id: 101, username: "simran", caption: "Beautiful day!", hashtag: "#nature", likes: 250, comments: 30, location: "Chandigarh" },
  { post_id: 102, username: "aman", caption: "Learning MongoDB today", hashtag: "#mongodb", likes: 180, comments: 20, location: "Delhi" },
  { post_id: 103, username: "priya", caption: "Amazing travel experience", hashtag: "#travel", likes: 520, comments: 75, location: "Manali" },
  { post_id: 104, username: "rahul", caption: "Big Data practical", hashtag: "#bigdata", likes: 150, comments: 15, location: "Amritsar" },
  { post_id: 105, username: "neha", caption: "Beautiful sunset", hashtag: "#nature", likes: 430, comments: 50, location: "Goa" },
  { post_id: 106, username: "simran", caption: "MongoDB practical work", hashtag: "#mongodb", likes: 320, comments: 40, location: "Chandigarh" }
])


db.comments.insertMany([
  { comment_id: 1, post_id: 101, username: "aman", comment: "Beautiful picture!" },
  { comment_id: 2, post_id: 101, username: "priya", comment: "Amazing!" },
  { comment_id: 3, post_id: 103, username: "simran", comment: "Nice place!" },
  { comment_id: 4, post_id: 105, username: "rahul", comment: "Wonderful sunset!" }
])


// Display all users

db.users.find()


// Display all posts

db.posts.find()


// Find posts by hashtag

db.posts.find({ hashtag: "#nature" })


// Posts with more than 300 likes

db.posts.find({ likes: { $gt: 300 } })


// Posts by simran

db.posts.find({ username: "simran" })


// Sort posts by likes

db.posts.find().sort({ likes: -1 })


// Top 3 most liked posts

db.posts.find().sort({ likes: -1 }).limit(3)


// Users with more than 1000 followers

db.users.find({ followers: { $gt: 1000 } })


// Update likes

db.posts.updateOne({ post_id: 101 }, { $set: { likes: 300 } })


// Increase followers

db.users.updateOne({ username: "simran" }, { $inc: { followers: 100 } })


// Create index on hashtag

db.posts.createIndex({ hashtag: 1 })


// Create index on username

db.posts.createIndex({ username: 1 })


// View all indexes

db.posts.getIndexes()


// Search using indexed hashtag

db.posts.find({ hashtag: "#mongodb" })


// Search using indexed username

db.posts.find({ username: "simran" })


// Remove hashtag index

db.posts.dropIndex("hashtag_1")


// View indexes again

db.posts.getIndexes()
