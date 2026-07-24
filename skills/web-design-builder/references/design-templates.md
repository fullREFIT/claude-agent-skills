# Design Templates

Ready-to-use starter templates for common web design types. Copy and customize for each project.


## SaaS Landing Page

Complete landing page with hero, features, pricing, and CTA sections.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Name - Your Tagline Here</title>
  <style>
    :root {
      --primary: #4F46E5;
      --primary-hover: #4338CA;
      --primary-light: #EEF2FF;
      --text: #1F2937;
      --text-muted: #6B7280;
      --bg: #FFFFFF;
      --bg-alt: #F9FAFB;
      --border: #E5E7EB;
      --success: #059669;
      --radius: 0.5rem;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      line-height: 1.6;
      color: var(--text);
      background: var(--bg);
    }

    .skip-link {
      position: absolute; top: -40px; left: 0;
      background: var(--primary); color: white;
      padding: 8px 16px; z-index: 100; text-decoration: none;
    }
    .skip-link:focus { top: 0; }

    :focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }

    .container { max-width: 1200px; margin-inline: auto; padding-inline: 1rem; }

    /* Header */
    .header {
      padding: 1rem 0;
      border-bottom: 1px solid var(--border);
      position: sticky; top: 0;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      z-index: 50;
    }

    .header .container { display: flex; align-items: center; justify-content: space-between; }

    .logo { font-size: 1.5rem; font-weight: 700; color: var(--primary); text-decoration: none; }

    .nav-links { display: flex; gap: 2rem; list-style: none; align-items: center; }
    .nav-links a { color: var(--text); text-decoration: none; font-weight: 500; }
    .nav-links a:hover { color: var(--primary); }

    .mobile-toggle {
      display: none; background: none; border: none;
      font-size: 1.5rem; cursor: pointer; padding: 0.5rem;
    }

    /* Buttons */
    .btn {
      display: inline-flex; align-items: center; gap: 0.5rem;
      padding: 0.75rem 1.5rem; border-radius: var(--radius);
      font-weight: 600; text-decoration: none; border: none;
      cursor: pointer; font: inherit; transition: all 0.2s;
    }
    .btn-primary { background: var(--primary); color: white; }
    .btn-primary:hover { background: var(--primary-hover); }
    .btn-outline { border: 2px solid var(--border); color: var(--text); background: transparent; }
    .btn-outline:hover { border-color: var(--primary); color: var(--primary); }

    /* Hero */
    .hero { padding: 5rem 0; text-align: center; }
    .hero h1 { font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; margin-bottom: 1.5rem; }
    .hero p { font-size: 1.25rem; color: var(--text-muted); max-width: 600px; margin-inline: auto; margin-bottom: 2rem; }
    .hero-cta { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }

    /* Features */
    .features { padding: 5rem 0; background: var(--bg-alt); }
    .section-header { text-align: center; margin-bottom: 3rem; }
    .section-header h2 { font-size: clamp(1.75rem, 3vw, 2.5rem); margin-bottom: 1rem; }
    .section-header p { color: var(--text-muted); max-width: 500px; margin-inline: auto; }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
      gap: 2rem;
    }

    .feature-card {
      background: white; padding: 2rem; border-radius: 12px;
      border: 1px solid var(--border); transition: box-shadow 0.2s;
    }
    .feature-card:hover { box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); }

    .feature-icon {
      width: 48px; height: 48px;
      background: var(--primary-light); border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      margin-bottom: 1rem; font-size: 1.5rem;
    }
    .feature-card h3 { margin-bottom: 0.5rem; }
    .feature-card p { color: var(--text-muted); }

    /* Pricing */
    .pricing { padding: 5rem 0; }
    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
      gap: 2rem; max-width: 900px; margin-inline: auto;
    }

    .price-card {
      border: 2px solid var(--border); border-radius: 12px;
      padding: 2rem; text-align: center;
    }
    .price-card.popular { border-color: var(--primary); position: relative; }
    .price-card.popular::before {
      content: 'Most Popular'; position: absolute; top: -14px; left: 50%;
      transform: translateX(-50%); background: var(--primary); color: white;
      padding: 4px 16px; border-radius: 20px; font-size: 0.875rem; font-weight: 600;
    }

    .price { font-size: 3rem; font-weight: 800; margin: 1rem 0; }
    .price span { font-size: 1rem; font-weight: 400; color: var(--text-muted); }

    .price-features { list-style: none; text-align: left; margin: 1.5rem 0; }
    .price-features li { padding: 0.5rem 0; border-bottom: 1px solid var(--border); }
    .price-features li::before { content: '✓ '; color: var(--success); font-weight: 700; }

    /* CTA */
    .cta { padding: 5rem 0; background: var(--primary); color: white; text-align: center; }
    .cta h2 { font-size: clamp(1.75rem, 3vw, 2.5rem); margin-bottom: 1rem; }
    .cta p { opacity: 0.9; margin-bottom: 2rem; max-width: 500px; margin-inline: auto; }
    .btn-white { background: white; color: var(--primary); }
    .btn-white:hover { background: var(--bg-alt); }

    /* Footer */
    .footer { padding: 2rem 0; border-top: 1px solid var(--border); text-align: center; color: var(--text-muted); }

    /* Mobile */
    @media (max-width: 768px) {
      .nav-links {
        display: none; position: absolute; top: 100%; left: 0; right: 0;
        background: white; flex-direction: column; padding: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); gap: 0.5rem;
      }
      .nav-links.active { display: flex; }
      .mobile-toggle { display: block; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
    }
  </style>
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <header class="header" role="banner">
    <div class="container">
      <a href="/" class="logo">ProductName</a>
      <button class="mobile-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      <ul class="nav-links" role="list">
        <li><a href="#features">Features</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#cta" class="btn btn-primary">Get Started</a></li>
      </ul>
    </div>
  </header>

  <main id="main">
    <section class="hero">
      <div class="container">
        <h1>Build Something Amazing</h1>
        <p>The fastest way to launch your next project. Simple, powerful, and built for teams.</p>
        <div class="hero-cta">
          <a href="#cta" class="btn btn-primary">Start Free Trial</a>
          <a href="#features" class="btn btn-outline">Learn More</a>
        </div>
      </div>
    </section>

    <section id="features" class="features">
      <div class="container">
        <div class="section-header">
          <h2>Everything You Need</h2>
          <p>Powerful features to help you build, launch, and grow.</p>
        </div>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon" aria-hidden="true">⚡</div>
            <h3>Lightning Fast</h3>
            <p>Optimized for speed with sub-second response times across all operations.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon" aria-hidden="true">🔒</div>
            <h3>Enterprise Security</h3>
            <p>Bank-grade encryption and SOC 2 compliance built into every layer.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon" aria-hidden="true">📊</div>
            <h3>Smart Analytics</h3>
            <p>Real-time insights and customizable dashboards to drive decisions.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="pricing" class="pricing">
      <div class="container">
        <div class="section-header">
          <h2>Simple Pricing</h2>
          <p>No hidden fees. Cancel anytime.</p>
        </div>
        <div class="pricing-grid">
          <div class="price-card">
            <h3>Starter</h3>
            <div class="price">$9<span>/mo</span></div>
            <ul class="price-features">
              <li>Up to 5 projects</li>
              <li>Basic analytics</li>
              <li>Email support</li>
            </ul>
            <a href="#" class="btn btn-outline" style="width: 100%; justify-content: center;">Choose Starter</a>
          </div>
          <div class="price-card popular">
            <h3>Pro</h3>
            <div class="price">$29<span>/mo</span></div>
            <ul class="price-features">
              <li>Unlimited projects</li>
              <li>Advanced analytics</li>
              <li>Priority support</li>
              <li>Team collaboration</li>
            </ul>
            <a href="#" class="btn btn-primary" style="width: 100%; justify-content: center;">Choose Pro</a>
          </div>
        </div>
      </div>
    </section>

    <section id="cta" class="cta">
      <div class="container">
        <h2>Ready to Get Started?</h2>
        <p>Join thousands of teams already using ProductName.</p>
        <a href="#" class="btn btn-white">Start Your Free Trial</a>
      </div>
    </section>
  </main>

  <footer class="footer" role="contentinfo">
    <div class="container">
      <p>&copy; 2026 ProductName. All rights reserved.</p>
    </div>
  </footer>

  <script>
    (function() {
      'use strict';
      const toggle = document.querySelector('.mobile-toggle');
      const nav = document.querySelector('.nav-links');
      if (toggle && nav) {
        toggle.addEventListener('click', function() {
          const expanded = this.getAttribute('aria-expanded') === 'true';
          this.setAttribute('aria-expanded', String(!expanded));
          nav.classList.toggle('active');
        });
      }
    })();
  </script>
</body>
</html>
```


## Contact Form

Accessible form with real-time validation and error handling.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us</title>
  <style>
    :root {
      --primary: #4F46E5;
      --primary-hover: #4338CA;
      --text: #1F2937;
      --text-muted: #6B7280;
      --bg: #F9FAFB;
      --border: #D1D5DB;
      --error: #DC2626;
      --success: #059669;
      --radius: 0.5rem;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); }
    :focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }

    .form-container {
      max-width: 560px; margin: 4rem auto; padding: 2.5rem;
      background: white; border-radius: 12px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .form-container h1 { font-size: 1.75rem; margin-bottom: 0.5rem; }
    .form-container > p { color: var(--text-muted); margin-bottom: 2rem; }

    .form-field { margin-bottom: 1.5rem; }

    label { display: block; margin-bottom: 0.5rem; font-weight: 600; font-size: 0.9375rem; }
    label .required { color: var(--error); }

    input, textarea, select {
      width: 100%; padding: 0.75rem 1rem;
      border: 2px solid var(--border); border-radius: var(--radius);
      font: inherit; font-size: 1rem; transition: border-color 0.2s;
    }
    input:focus, textarea:focus { border-color: var(--primary); }
    input[aria-invalid="true"], textarea[aria-invalid="true"] { border-color: var(--error); }

    .hint { display: block; margin-top: 0.25rem; font-size: 0.875rem; color: var(--text-muted); }
    .error-msg { display: block; margin-top: 0.25rem; font-size: 0.875rem; color: var(--error); }

    .btn-submit {
      width: 100%; padding: 0.875rem; background: var(--primary); color: white;
      border: none; border-radius: var(--radius); font: inherit; font-weight: 600;
      font-size: 1rem; cursor: pointer; transition: background 0.2s;
    }
    .btn-submit:hover { background: var(--primary-hover); }

    .success-msg { padding: 1rem; background: #D1FAE5; color: #065F46; border-radius: var(--radius); margin-bottom: 1rem; }

    @media (prefers-reduced-motion: reduce) {
      * { transition-duration: 0.01ms !important; }
    }
  </style>
</head>
<body>
  <main class="form-container">
    <h1>Contact Us</h1>
    <p>Fill out the form below and we'll get back to you within 24 hours.</p>

    <form id="contact-form" novalidate>
      <div class="form-field">
        <label for="name">Name <span class="required" aria-label="required">*</span></label>
        <input type="text" id="name" name="name" required aria-required="true" aria-describedby="name-error" autocomplete="name" />
        <span id="name-error" class="error-msg" role="alert" hidden>Please enter your name</span>
      </div>

      <div class="form-field">
        <label for="email">Email <span class="required" aria-label="required">*</span></label>
        <input type="email" id="email" name="email" required aria-required="true" aria-describedby="email-hint email-error" autocomplete="email" />
        <span id="email-hint" class="hint">We'll never share your email with anyone.</span>
        <span id="email-error" class="error-msg" role="alert" hidden>Please enter a valid email address</span>
      </div>

      <div class="form-field">
        <label for="subject">Subject</label>
        <select id="subject" name="subject">
          <option value="">Select a topic...</option>
          <option value="general">General Inquiry</option>
          <option value="support">Technical Support</option>
          <option value="billing">Billing Question</option>
          <option value="feedback">Feedback</option>
        </select>
      </div>

      <div class="form-field">
        <label for="message">Message <span class="required" aria-label="required">*</span></label>
        <textarea id="message" name="message" rows="5" required aria-required="true" aria-describedby="message-error"></textarea>
        <span id="message-error" class="error-msg" role="alert" hidden>Please enter a message</span>
      </div>

      <button type="submit" class="btn-submit">Send Message</button>
    </form>
  </main>

  <script>
    (function() {
      'use strict';
      const form = document.getElementById('contact-form');

      form.addEventListener('submit', function(e) {
        e.preventDefault();
        clearErrors();

        let valid = true;
        let firstInvalid = null;

        const name = document.getElementById('name');
        if (!name.value.trim()) { showError(name, 'name-error'); valid = false; firstInvalid = firstInvalid || name; }

        const email = document.getElementById('email');
        if (!email.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
          showError(email, 'email-error'); valid = false; firstInvalid = firstInvalid || email;
        }

        const message = document.getElementById('message');
        if (!message.value.trim()) { showError(message, 'message-error'); valid = false; firstInvalid = firstInvalid || message; }

        if (valid) {
          const success = document.createElement('div');
          success.className = 'success-msg';
          success.setAttribute('role', 'status');
          success.textContent = 'Thank you! Your message has been sent successfully.';
          form.insertBefore(success, form.firstChild);
          form.reset();
        } else if (firstInvalid) {
          firstInvalid.focus();
        }
      });

      function showError(field, errorId) {
        field.setAttribute('aria-invalid', 'true');
        document.getElementById(errorId).hidden = false;
      }

      function clearErrors() {
        form.querySelectorAll('.error-msg').forEach(el => el.hidden = true);
        form.querySelectorAll('[aria-invalid]').forEach(el => el.removeAttribute('aria-invalid'));
        const existing = form.querySelector('.success-msg');
        if (existing) existing.remove();
      }
    })();
  </script>
</body>
</html>
```


## Admin Dashboard

Responsive dashboard layout with sidebar, stats cards, and data table.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard</title>
  <style>
    :root {
      --sidebar-w: 250px;
      --header-h: 60px;
      --primary: #4F46E5;
      --text: #1F2937;
      --text-muted: #6B7280;
      --bg: #F3F4F6;
      --card-bg: #FFFFFF;
      --sidebar-bg: #1F2937;
      --sidebar-text: #D1D5DB;
      --sidebar-active: #374151;
      --border: #E5E7EB;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); }
    :focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }

    .dashboard {
      display: grid;
      grid-template-areas: "sidebar header" "sidebar main";
      grid-template-columns: var(--sidebar-w) 1fr;
      grid-template-rows: var(--header-h) 1fr;
      min-height: 100vh;
    }

    /* Sidebar */
    .sidebar {
      grid-area: sidebar; background: var(--sidebar-bg); color: var(--sidebar-text); padding: 1.5rem 1rem;
    }
    .sidebar h2 { color: white; font-size: 1.25rem; margin-bottom: 2rem; padding-left: 0.75rem; }
    .sidebar nav ul { list-style: none; }
    .sidebar nav a {
      display: flex; align-items: center; gap: 0.75rem;
      padding: 0.75rem; color: var(--sidebar-text); text-decoration: none;
      border-radius: 0.375rem; transition: background 0.2s; margin-bottom: 0.25rem;
    }
    .sidebar nav a:hover, .sidebar nav a[aria-current="page"] {
      background: var(--sidebar-active); color: white;
    }

    /* Header */
    .dash-header {
      grid-area: header; background: var(--card-bg);
      border-bottom: 1px solid var(--border); padding: 0 2rem;
      display: flex; align-items: center; justify-content: space-between;
    }
    .dash-header h1 { font-size: 1.25rem; }
    .mobile-sidebar-toggle { display: none; background: none; border: none; font-size: 1.5rem; cursor: pointer; }

    /* Main */
    .main { grid-area: main; padding: 2rem; overflow-y: auto; }

    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr));
      gap: 1.5rem; margin-bottom: 2rem;
    }
    .stat-card {
      background: var(--card-bg); padding: 1.5rem; border-radius: 0.5rem;
      border: 1px solid var(--border);
    }
    .stat-label { font-size: 0.875rem; color: var(--text-muted); margin-bottom: 0.25rem; }
    .stat-value { font-size: 2rem; font-weight: 700; }
    .stat-change { font-size: 0.875rem; margin-top: 0.25rem; }
    .stat-change.positive { color: #059669; }
    .stat-change.negative { color: #DC2626; }

    /* Table */
    .table-card {
      background: var(--card-bg); border-radius: 0.5rem;
      border: 1px solid var(--border); overflow: hidden;
    }
    .table-card h2 { padding: 1.25rem 1.5rem; font-size: 1.125rem; border-bottom: 1px solid var(--border); }

    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 0.75rem 1.5rem; text-align: left; border-bottom: 1px solid var(--border); }
    th { font-weight: 600; font-size: 0.875rem; color: var(--text-muted); background: var(--bg); }
    tr:last-child td { border-bottom: none; }

    .badge {
      display: inline-block; padding: 0.25rem 0.75rem; border-radius: 9999px;
      font-size: 0.75rem; font-weight: 600;
    }
    .badge-success { background: #D1FAE5; color: #065F46; }
    .badge-warning { background: #FEF3C7; color: #92400E; }
    .badge-danger { background: #FEE2E2; color: #991B1B; }

    @media (max-width: 768px) {
      .dashboard {
        grid-template-areas: "header" "main";
        grid-template-columns: 1fr;
      }
      .sidebar {
        position: fixed; left: -260px; top: 0; bottom: 0; width: var(--sidebar-w);
        z-index: 100; transition: left 0.3s;
      }
      .sidebar.active { left: 0; }
      .mobile-sidebar-toggle { display: block; }

      /* Responsive table */
      .table-card { overflow-x: auto; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { transition-duration: 0.01ms !important; }
    }
  </style>
</head>
<body>
  <div class="dashboard">
    <aside class="sidebar">
      <h2>AppName</h2>
      <nav aria-label="Dashboard navigation">
        <ul>
          <li><a href="#" aria-current="page">📊 Overview</a></li>
          <li><a href="#">👥 Users</a></li>
          <li><a href="#">📈 Analytics</a></li>
          <li><a href="#">⚙️ Settings</a></li>
        </ul>
      </nav>
    </aside>

    <header class="dash-header" role="banner">
      <button class="mobile-sidebar-toggle" aria-label="Toggle sidebar" aria-expanded="false">☰</button>
      <h1>Dashboard Overview</h1>
      <span>Welcome, User</span>
    </header>

    <main class="main">
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-label">Total Users</div>
          <div class="stat-value">2,847</div>
          <div class="stat-change positive">↑ 12% from last month</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Revenue</div>
          <div class="stat-value">$34,521</div>
          <div class="stat-change positive">↑ 8% from last month</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Active Sessions</div>
          <div class="stat-value">1,203</div>
          <div class="stat-change negative">↓ 3% from last week</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Uptime</div>
          <div class="stat-value">99.9%</div>
          <div class="stat-change positive">Stable</div>
        </div>
      </div>

      <div class="table-card">
        <h2>Recent Activity</h2>
        <table>
          <thead>
            <tr>
              <th scope="col">User</th>
              <th scope="col">Action</th>
              <th scope="col">Status</th>
              <th scope="col">Date</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Alice Johnson</td>
              <td>Created new project</td>
              <td><span class="badge badge-success">Completed</span></td>
              <td>Feb 13, 2026</td>
            </tr>
            <tr>
              <td>Bob Smith</td>
              <td>Updated settings</td>
              <td><span class="badge badge-warning">Pending</span></td>
              <td>Feb 12, 2026</td>
            </tr>
            <tr>
              <td>Carol Davis</td>
              <td>Deleted account</td>
              <td><span class="badge badge-danger">Attention</span></td>
              <td>Feb 11, 2026</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>

  <script>
    (function() {
      'use strict';
      const toggle = document.querySelector('.mobile-sidebar-toggle');
      const sidebar = document.querySelector('.sidebar');
      if (toggle && sidebar) {
        toggle.addEventListener('click', function() {
          const expanded = this.getAttribute('aria-expanded') === 'true';
          this.setAttribute('aria-expanded', String(!expanded));
          sidebar.classList.toggle('active');
        });
      }
    })();
  </script>
</body>
</html>
```

These templates provide production-quality starting points. Customize colors, content, and structure for each project.
