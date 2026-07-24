# Framework Guide

Setup and patterns for supported CSS/JS frameworks. Choose based on project requirements.


## Tailwind CSS (CDN — No Build Step)

### Setup

```html
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            primary: { DEFAULT: '#4F46E5', hover: '#4338CA', light: '#EEF2FF' },
          },
          fontFamily: {
            sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
          },
        },
      },
    }
  </script>
</head>
```

### Common Patterns

**Responsive navigation:**
```html
<nav class="flex items-center justify-between p-4 bg-white shadow-sm">
  <a href="/" class="text-xl font-bold text-primary">Logo</a>

  <!-- Desktop nav -->
  <ul class="hidden md:flex gap-6">
    <li><a href="#features" class="text-gray-700 hover:text-primary font-medium">Features</a></li>
    <li><a href="#pricing" class="text-gray-700 hover:text-primary font-medium">Pricing</a></li>
    <li><a href="#contact" class="text-gray-700 hover:text-primary font-medium">Contact</a></li>
  </ul>

  <!-- Mobile toggle -->
  <button class="md:hidden p-2" aria-label="Toggle menu" aria-expanded="false">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
    </svg>
  </button>
</nav>
```

**Hero section:**
```html
<section class="py-20 px-4 text-center">
  <div class="max-w-3xl mx-auto">
    <h1 class="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6">
      Build Something Amazing
    </h1>
    <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
      The best solution for your business needs.
    </p>
    <div class="flex gap-4 justify-center flex-wrap">
      <a href="#signup" class="bg-primary hover:bg-primary-hover text-white font-semibold py-3 px-8 rounded-lg transition-colors">
        Get Started
      </a>
      <a href="#demo" class="border-2 border-gray-300 hover:border-primary text-gray-700 font-semibold py-3 px-8 rounded-lg transition-colors">
        Watch Demo
      </a>
    </div>
  </div>
</section>
```

**Feature cards grid:**
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
  <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
    <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
      <span class="text-2xl">⚡</span>
    </div>
    <h3 class="text-lg font-semibold mb-2">Feature Title</h3>
    <p class="text-gray-600">Feature description goes here with helpful details.</p>
  </div>
</div>
```

**Accessible form with Tailwind:**
```html
<form class="max-w-lg mx-auto space-y-6" novalidate>
  <div>
    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">
      Email <span class="text-red-500" aria-label="required">*</span>
    </label>
    <input
      type="email" id="email" name="email"
      required aria-required="true" aria-describedby="email-error"
      class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-colors"
    />
    <p id="email-error" class="mt-1 text-sm text-red-600 hidden" role="alert">
      Please enter a valid email address
    </p>
  </div>

  <button type="submit" class="w-full bg-primary hover:bg-primary-hover text-white font-semibold py-3 px-6 rounded-lg transition-colors focus:ring-2 focus:ring-primary/50 focus:ring-offset-2">
    Submit
  </button>
</form>
```

### Tailwind Dark Mode

```html
<script>
  tailwind.config = {
    darkMode: 'class',
    // ...theme config
  }
</script>

<!-- Toggle button -->
<button onclick="document.documentElement.classList.toggle('dark')" aria-label="Toggle dark mode">
  🌓
</button>

<!-- Elements with dark variants -->
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
  <p class="text-gray-600 dark:text-gray-400">Adapts to theme.</p>
</div>
```


## Alpine.js

### Setup

```html
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js"></script>
```

### Common Patterns

**Toggle menu:**
```html
<div x-data="{ open: false }">
  <button @click="open = !open" :aria-expanded="open" aria-controls="mobile-menu">
    Menu
  </button>
  <nav id="mobile-menu" x-show="open" x-transition @click.outside="open = false">
    <a href="#features">Features</a>
    <a href="#pricing">Pricing</a>
  </nav>
</div>
```

**Tabs:**
```html
<div x-data="{ activeTab: 'tab1' }">
  <div role="tablist">
    <button role="tab" :aria-selected="activeTab === 'tab1'" @click="activeTab = 'tab1'"
      :class="activeTab === 'tab1' ? 'border-b-2 border-primary text-primary' : 'text-gray-500'">
      Tab 1
    </button>
    <button role="tab" :aria-selected="activeTab === 'tab2'" @click="activeTab = 'tab2'"
      :class="activeTab === 'tab2' ? 'border-b-2 border-primary text-primary' : 'text-gray-500'">
      Tab 2
    </button>
  </div>

  <div role="tabpanel" x-show="activeTab === 'tab1'">Content 1</div>
  <div role="tabpanel" x-show="activeTab === 'tab2'">Content 2</div>
</div>
```

**Modal:**
```html
<div x-data="{ showModal: false }">
  <button @click="showModal = true">Open Modal</button>

  <div x-show="showModal" x-transition.opacity class="fixed inset-0 bg-black/50 z-40"
    @click="showModal = false" aria-hidden="true"></div>

  <dialog x-show="showModal" x-transition
    class="fixed z-50 bg-white rounded-xl p-6 shadow-xl max-w-md mx-auto"
    @keydown.escape="showModal = false" x-trap.noscroll="showModal">
    <h2>Modal Title</h2>
    <p>Modal content here.</p>
    <button @click="showModal = false">Close</button>
  </dialog>
</div>
```

**Form with validation:**
```html
<form x-data="{ name: '', email: '', submitted: false }" @submit.prevent="submitted = true" novalidate>
  <div>
    <label for="name">Name *</label>
    <input id="name" x-model="name" required :aria-invalid="submitted && !name" />
    <p x-show="submitted && !name" class="text-red-600" role="alert">Name is required</p>
  </div>

  <div>
    <label for="email">Email *</label>
    <input id="email" type="email" x-model="email" required />
    <p x-show="submitted && !email" class="text-red-600" role="alert">Email is required</p>
  </div>

  <button type="submit">Submit</button>
</form>
```


## HTMX

### Setup

```html
<script src="https://unpkg.com/htmx.org@2/dist/htmx.min.js"></script>
```

### Common Patterns

HTMX enables server-driven interactivity. Best for forms, search, and CRUD interfaces when a backend is available.

**Search with live results:**
```html
<input type="search" name="q"
  hx-get="/search"
  hx-trigger="input changed delay:300ms"
  hx-target="#results"
  hx-indicator="#spinner"
  placeholder="Search..." />

<span id="spinner" class="htmx-indicator">Loading...</span>
<div id="results"></div>
```

**Form submission:**
```html
<form hx-post="/contact" hx-target="#form-response" hx-swap="innerHTML">
  <label for="message">Message</label>
  <textarea id="message" name="message" required></textarea>
  <button type="submit">Send</button>
</form>
<div id="form-response"></div>
```

**Infinite scroll:**
```html
<div id="items">
  <!-- Items rendered here -->
  <div hx-get="/items?page=2" hx-trigger="revealed" hx-swap="afterend">
    Loading more...
  </div>
</div>
```

**Note:** HTMX requires a server backend. For static mockups, use it with placeholder responses or recommend it for production integration.


## React (CDN — No Build Step)

### Setup

```html
<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
```

### Common Patterns

**Component with state:**
```html
<div id="app"></div>
<script type="text/babel">
  function App() {
    const [count, setCount] = React.useState(0);
    const [isOpen, setIsOpen] = React.useState(false);

    return (
      <div className="container">
        <h1>React App</h1>
        <button onClick={() => setCount(c => c + 1)}>
          Count: {count}
        </button>

        <button
          onClick={() => setIsOpen(!isOpen)}
          aria-expanded={isOpen}
          aria-controls="panel"
        >
          Toggle Panel
        </button>

        {isOpen && (
          <div id="panel" role="region">
            <p>Panel content</p>
          </div>
        )}
      </div>
    );
  }

  const root = ReactDOM.createRoot(document.getElementById('app'));
  root.render(<App />);
</script>
```

**Note:** CDN React is suitable for prototypes and mockups. For production, recommend a build tool (Vite, Next.js).


## Framework Comparison

| Feature | Vanilla | Tailwind | Alpine.js | HTMX | React |
|---------|---------|----------|-----------|------|-------|
| Bundle size | 0 KB | ~300KB (CDN) | ~15 KB | ~14 KB | ~140 KB |
| Build step needed | No | No (CDN) | No | No | No (CDN) |
| Learning curve | Low | Low | Low | Low | Medium |
| Interactivity | Manual JS | Manual JS | Declarative | Server-driven | Component state |
| Best for | Static sites | Rapid styling | Light interactivity | Server-connected | Complex SPAs |
| Accessibility | Manual | Manual | Manual | Manual | Manual |
| Dark mode | CSS-only | Built-in `dark:` | CSS-only | CSS-only | State-managed |

### When to Combine Frameworks

Common combinations:
- **Tailwind + Alpine.js** — Best for most mockups. Tailwind handles styling, Alpine handles interactivity.
- **Tailwind + HTMX** — For server-connected prototypes with beautiful UI.
- **Vanilla + minimal JS** — For maximum performance and zero dependencies.
