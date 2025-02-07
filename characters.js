const sqlite3 = require('sqlite3');
const fs = require('fs');
const path = require('path');

// List of characters you want to extract (e.g., ["汉", "字", "你"])
const targetCharacters = ['汉', '字', '你'];

// Open the database
const db = new sqlite3.Database('data.db');

// Create an output folder if it doesn't exist
const outputDir = path.join(__dirname, '..', 'output');
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

// Query the database for each character
targetCharacters.forEach((character) => {
  db.get(
    'SELECT * FROM glyphs WHERE character = ?',
    [character],
    (err, row) => {
      if (err) throw err;
      if (!row) {
        console.warn(`Character "${character}" not found in the database.`);
        return;
      }

      // Parse and format the data
      const data = {
        character: row.character,
        strokes: JSON.parse(row.strokes),
        medians: JSON.parse(row.medians),
      };

      // Save to a JSON file
      const outputPath = path.join(outputDir, `${character}.json`);
      fs.writeFileSync(outputPath, JSON.stringify(data, null, 2));
      console.log(`Saved data for "${character}" to ${outputPath}`);
    }
  );
});

// Close the database connection
db.close();