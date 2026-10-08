const assert = require('assert');
const fs = require('fs');
const path = require('path');
assert.ok(fs.existsSync(path.join(__dirname, '..', 'package.json')));
assert.ok(fs.existsSync(path.join(__dirname, '..', 'src', 'DiffView.tsx')));
process.exit(0);
