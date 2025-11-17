# 🎨 **`static/` — Front-End Static Assets**

The `static/` directory contains all static front-end assets used by the **LLMOps Celebrity Detector**.
These files provide styling, animations, and visual effects that enhance the user interface rendered through the Flask application.

All files in this folder are served directly by Flask and are referenced in templates through `url_for('static', ...)`.

## 📁 **Folder Structure**

```text
static/
└── style.css
```

## 🧩 **Components**

### `style.css`

This file defines all custom CSS used throughout the application, including:

* Global typographic styles
* Black page background configuration
* Button hover transitions
* Image hover effects
* The neon glowing title effect
* Styled answer box (indigo gradient container)
* Keyframe animations for subtle fade-in effects

The stylesheet complements TailwindCSS, allowing for custom visual touches that Tailwind classes alone cannot provide.

## 🚀 **Purpose of the `static/` Layer**

The `static/` directory handles all visual enhancements and custom client-side styling, providing:

* Consistent look and feel beyond default Tailwind utilities
* Custom animations and glow effects
* A flexible foundation for future UI expansions such as:

  * Component-specific styles
  * Enhanced hover states
  * Additional transitions
  * Icons, images, or JavaScript scripts

It ensures that the project’s UI can scale visually while keeping logic separate from presentation.

## ✔️ **Usage Example**

To load a CSS file in your template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

To reference future assets (images, logos, scripts), you can use:

```html
<img src="{{ url_for('static', filename='logo.png') }}">
<script src="{{ url_for('static', filename='script.js') }}"></script>
```
