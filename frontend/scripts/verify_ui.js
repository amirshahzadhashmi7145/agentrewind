const assert = require('assert');
const fs = require('fs');
const path = require('path');
const pkg = path.join(__dirname, '..', 'package.json');
assert.ok(fs.existsSync(pkg), 'package.json missing at ' + pkg);
assert.ok(fs.existsSync(path.join(__dirname, '..', 'src', 'App.tsx')));
process.exit(0);
