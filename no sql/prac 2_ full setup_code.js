/*
================================================================================
 PRACTICAL 2: MongoDB Aggregation on the Zip Code Dataset (Windows)
================================================================================
 Dataset  : http://media.mongodb.org/zips.json  (29353 documents)
 Database : zipcode_db
 Collection: zipcodes
================================================================================
*/


/*
================================================================================
 PART 1: WHAT TO DOWNLOAD (do this first)
================================================================================
 1. MongoDB Community Server (MSI installer)
    - Choose "Complete" setup
    - Tick "Install MongoDB as a Service"
    - Download: https://www.mongodb.com/try/download/community

 2. MongoDB Shell (mongosh)
    - Download: https://www.mongodb.com/try/download/shell

 3. MongoDB Database Tools (this contains mongoimport)
    - Choose the ZIP package for Windows
    - Extract it, for example to:  D:\New folder\mongodb-database-tools-windows-x86_64-100.20.0
    - Download: https://www.mongodb.com/try/download/database-tools

 4. The dataset (zips.json)
    - Open Command Prompt and run:
        mkdir D:\data
        curl -o D:\data\zips.json http://media.mongodb.org/zips.json
    - Or open the link in a browser, press Ctrl+S, and save it to D:\data\zips.json
*/


/*
================================================================================
 PART 2: PATH SETUP (very important)
================================================================================
 Goal: make Command Prompt find "mongoimport" from any folder.

 Step 1. Open the folder that contains mongoimport.exe. It is the "bin" folder:
         D:\New folder\mongodb-database-tools-windows-x86_64-100.20.0\bin

 Step 2. Click the address bar of that folder and copy the full path.

 Step 3. Press the Windows key and search:  Environment Variables
         Open "Edit the system environment variables".

 Step 4. Click "Environment Variables".

 Step 5. Under "System variables" select "Path", then click "Edit".

 Step 6. Click "New" and paste the bin folder path:
         D:\New folder\mongodb-database-tools-windows-x86_64-100.20.0\bin

 Step 7. Click OK on every window.

 Step 8. CLOSE all Command Prompt / PowerShell windows and open a new one.

 Step 9. Test:
         mongoimport --version
         (If a version prints, the path is correct.)

 If you do not want to set the PATH, open the bin folder, click the address
 bar, type  cmd  and press Enter. A Command Prompt opens already inside bin.

 Temporary path (only for the current window):
   CMD         :  set PATH=%PATH%;D:\New folder\mongodb-database-tools-windows-x86_64-100.20.0\bin
   PowerShell  :  $env:Path += ";D:\New folder\mongodb-database-tools-windows-x86_64-100.20.0\bin"

 Do the same for mongosh if "mongosh" is not recognized.
*/


/*
================================================================================
 PART 3: IMPORT THE DATA
================================================================================
 Run this in COMMAND PROMPT (CMD), NOT inside mongosh.
 If the path has spaces, put it in double quotes.

   mongoimport --db zipcode_db --collection zipcodes --file D:\data\zips.json

 Expected result:
   29353 document(s) imported successfully. 0 document(s) failed to import.

 If you see "E11000 duplicate key error ... 0 imported, 29353 failed":
 the data is already imported. This is not a problem.
 To start fresh, run inside mongosh:  db.zipcodes.drop()  and import again.
*/


/*
================================================================================
 PART 4: OPEN MONGOSH AND SELECT THE DATABASE
================================================================================
 In CMD run:
   mongosh

 Then run these two lines, one at a time:
*/

use zipcode_db

db.zipcodes.countDocuments()
// Expected output: 29353

db.zipcodes.findOne()
// Shows one sample record


/*
================================================================================
 PART 5: QUERIES (paste ONE block at a time)
 Note: mongosh shows 20 results at a time. Type  it  and press Enter for more.
================================================================================
*/


// ------------------------------------------------------------------------------
// QUERY A: Find all states that have a city called "BOSTON"
// ------------------------------------------------------------------------------

db.zipcodes.aggregate([
  {
    $match: { city: "BOSTON" }
  },
  {
    $group: { _id: "$state" }
  },
  {
    $project: { _id: 0, state: "$_id" }
  }
])

// Expected output (states): TX, NY, MA, PA, GA, KY, VA


// ------------------------------------------------------------------------------
// QUERY A2: Find all states and cities whose names include "BOST"
// ------------------------------------------------------------------------------

db.zipcodes.aggregate([
  {
    $match: { city: { $regex: "BOST", $options: "i" } }
  },
  {
    $group: { _id: { state: "$state", city: "$city" } }
  },
  {
    $project: { _id: 0, state: "$_id.state", city: "$_id.city" }
  },
  {
    $sort: { state: 1, city: 1 }
  }
])

// Expected output (sample): { state: 'MA', city: 'BOSTON' }, NEW BOSTON, SOUTH BOSTON, ...


// ------------------------------------------------------------------------------
// QUERY B: City in each state with the most ZIP codes,
//          ranked by city population
// ------------------------------------------------------------------------------

db.zipcodes.aggregate([
  {
    $group: {
      _id: { state: "$state", city: "$city" },
      zipCodes: { $sum: 1 },
      population: { $sum: "$pop" }
    }
  },
  {
    $sort: { "_id.state": 1, zipCodes: -1 }
  },
  {
    $group: {
      _id: "$_id.state",
      city: { $first: "$_id.city" },
      zipCodes: { $first: "$zipCodes" },
      population: { $first: "$population" }
    }
  },
  {
    $sort: { population: -1 }
  },
  {
    $project: {
      _id: 0,
      state: "$_id",
      city: 1,
      zipCodes: 1,
      population: 1
    }
  }
])

// Expected output (top rows): CHICAGO (IL), LOS ANGELES (CA), HOUSTON (TX), ...
// Type  it  for the next page.


// ------------------------------------------------------------------------------
// SPATIAL INFORMATION (loc field)
// ------------------------------------------------------------------------------

db.zipcodes.findOne({}, { city: 1, state: 1, loc: 1 })

// loc[0] = longitude, loc[1] = latitude
