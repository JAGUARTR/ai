// PRACTICAL 2 - MongoDB zip code aggregation (run inside mongosh)
// Import first (in normal CMD, not mongosh):
// mongoimport --db zipcode_db --collection zipcodes --file zips.json

use zipcode_db

db.zipcodes.countDocuments()

db.zipcodes.findOne()


// A1. States that have a city called BOSTON

db.zipcodes.aggregate([
  { $match: { city: "BOSTON" } },
  { $group: { _id: "$state" } },
  { $project: { _id: 0, state: "$_id" } }
])


// A2. All states and cities containing BOST

db.zipcodes.aggregate([
  { $match: { city: { $regex: "BOST", $options: "i" } } },
  { $group: { _id: { state: "$state", city: "$city" } } },
  { $project: { _id: 0, state: "$_id.state", city: "$_id.city" } },
  { $sort: { state: 1, city: 1 } }
])


// B. City with most zip codes in each state, ranked by population

db.zipcodes.aggregate([
  {
    $group: {
      _id: { state: "$state", city: "$city" },
      zipCodes: { $sum: 1 },
      population: { $sum: "$pop" }
    }
  },
  { $sort: { "_id.state": 1, zipCodes: -1 } },
  {
    $group: {
      _id: "$_id.state",
      city: { $first: "$_id.city" },
      zipCodes: { $first: "$zipCodes" },
      population: { $first: "$population" }
    }
  },
  { $sort: { population: -1 } },
  { $project: { _id: 0, state: "$_id", city: 1, zipCodes: 1, population: 1 } }
])


// C. Spatial information (loc = [longitude, latitude])

db.zipcodes.findOne({}, { city: 1, state: 1, loc: 1 })


// C2. Spatial query: 5 zip codes nearest to Boston

db.zipcodes.createIndex({ loc: "2d" })

db.zipcodes.find({ loc: { $near: [-71.018378, 42.358894] } }, { city: 1, state: 1, loc: 1 }).limit(5)
