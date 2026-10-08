const assert = require('assert');
const fs = require('fs');
const path = require('path');
const pkg = path.join(__dirname, '..', 'package.json');
assert.ok(fs.existsSync(pkg));
assert.ok(fs.existsSync(path.join(__dirname, '..', 'src', 'App.tsx')));
assert.ok(fs.existsSync(path.join(__dirname, '..', 'src', 'VirtualTree.tsx')));
process.exit(0);
