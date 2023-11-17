# OpenTTDLab

Python framework for running reproducible experiments using OpenTTD

## Python

### Installation

```bash
python3 -m venv .env
.env/bin/pip install -r requirements.txt
```

### Usage

#### CLI-based interactive view

```bash
.env/bin/python -m savegame_reader <location-of-your-savegame>
```

![image](docs/example.png)

#### Export to JSON

```bash
.env/bin/python -m savegame_reader --export-json <location-of-your-savegame>
```

## Rust / Web

### Installation (Rust)

Have latest rust installed, and install `wasm-pack` (with `cargo install wasm-pack`).

```bash
cd webapp/xz-rust
wasm-pack build
```

### Installation (Web)

(depends on Rust)

```bash
cd webapp/web
npm install
npm run build
```

Alternatively for the last step, you can do `npm start` for development.
