# VIBE CODING PROJECT BUILDER — CUSTOM INSTRUCTIONS
## Part 3 of 3: Autonomous Task Templates, QA, & Best Practices

---

## AUTONOMOUS TASK SPECIFICATION TEMPLATES

### **Template 1: Complete Feature Build**

```bash
& implement [FEATURE NAME]:
  
  DATABASE (if needed):
  - create table [table_name] with fields: [list fields]
  - add indexes on: [list indexed fields]
  - create RLS policies: [describe policies]
  - add foreign keys: [describe relationships]
  
  API ROUTES:
  - GET /api/[resource] - [description]
  - POST /api/[resource] - [description]
  - GET /api/[resource]/[id] - [description]
  - PUT /api/[resource]/[id] - [description]
  - DELETE /api/[resource]/[id] - [description]
  - all routes use zod validation
  - include error handling
  
  PAGES:
  - /app/[path]/page.tsx - [description]
  - /app/[path]/[id]/page.tsx - [description]
  
  COMPONENTS:
  - [ComponentName] - [description]
  - [AnotherComponent] - [description]
  
  FEATURES:
  - [feature 1]
  - [feature 2]
  - [feature 3]
  
  STYLING:
  - use Tailwind CSS
  - follow shadcn/ui patterns
  - mobile responsive
  
  QUALITY:
  - follow CLAUDE.md standards
  - add error handling for all async operations
  - include loading and error states
  - test locally with npm run build
  
  GIT:
  - branch: feature/[feature-name]
  - commit with descriptive messages
  - push to GitHub when complete
```

### **Template 2: UI Page/Component**

```bash
& create [PAGE/COMPONENT NAME]:
  
  LAYOUT:
  - [describe layout structure]
  - [list main sections]
  
  COMPONENTS:
  - [Component 1] - [description and props]
  - [Component 2] - [description and props]
  
  FEATURES:
  - [interactive feature 1]
  - [interactive feature 2]
  
  DATA FETCHING (if needed):
  - fetch from [API endpoint]
  - handle loading state
  - handle error state
  - display [describe what to show]
  
  STYLING:
  - [color scheme, if specific]
  - [layout approach: grid/flex/etc]
  - responsive breakpoints: mobile (< 768px), tablet (768-1024px), desktop (> 1024px)
  - use Tailwind CSS
  - follow component patterns in /components/shared
  
  INTERACTIONS:
  - [describe user interactions]
  - [describe state changes]
  
  ACCESSIBILITY:
  - proper semantic HTML
  - ARIA labels where needed
  - keyboard navigation support
  
  QUALITY:
  - follow CLAUDE.md standards
  - mobile-first responsive design
  - test on multiple screen sizes
  
  GIT:
  - branch: feature/[name]
  - commit when complete
```

### **Template 3: API Integration**

```bash
& integrate [EXTERNAL SERVICE]:
  
  SETUP:
  - install required packages: [list npm packages]
  - add environment variables to .env.example
  - create client in /lib/[service].ts
  
  IMPLEMENTATION:
  - [function 1] - [description]
  - [function 2] - [description]
  - [function 3] - [description]
  
  ERROR HANDLING:
  - retry logic with exponential backoff
  - log errors appropriately
  - graceful degradation if service unavailable
  
  USAGE:
  - integrate in [location 1]
  - integrate in [location 2]
  
  TESTING:
  - test all functions with valid inputs
  - test error scenarios
  - verify rate limiting works
  
  DOCUMENTATION:
  - add setup instructions to README
  - document API usage in comments
  - include example calls
  
  GIT:
  - branch: feature/[service]-integration
  - commit when complete
```

### **Template 4: Database Schema & Migration**

```bash
& create database schema for [FEATURE]:
  
  TABLES:
  - [table_1]:
    - fields: [list with types]
    - primary key: [field]
    - foreign keys: [relationships]
    - indexes: [fields to index]
    - RLS policies: [describe]
  
  - [table_2]:
    - fields: [list with types]
    - primary key: [field]
    - foreign keys: [relationships]
    - indexes: [fields to index]
    - RLS policies: [describe]
  
  FUNCTIONS/TRIGGERS:
  - [function_name] - [purpose]
  - [trigger_name] - [when it fires]
  
  TYPE GENERATION:
  - run: npx supabase gen types typescript --linked > types/database.ts
  - update Database interface
  
  MIGRATION FILE:
  - create migration in /supabase/migrations/
  - include rollback instructions in comments
  
  DOCUMENTATION:
  - document schema in comments
  - explain RLS policies
  - note any performance considerations
  
  GIT:
  - branch: feature/[feature]-schema
  - commit migration file
```

### **Template 5: Refactoring/Cleanup**

```bash
& refactor [COMPONENT/FEATURE]:
  
  GOALS:
  - [improvement goal 1]
  - [improvement goal 2]
  - [improvement goal 3]
  
  CHANGES:
  - [specific change 1]
  - [specific change 2]
  - [specific change 3]
  
  CONSTRAINTS:
  - maintain existing functionality (no breaking changes)
  - preserve all test coverage
  - keep same API interface (if applicable)
  
  TESTING:
  - verify all existing tests pass
  - test manually: [list critical paths]
  - ensure no regressions
  
  QUALITY:
  - improve code readability
  - add comments for complex logic
  - follow CLAUDE.md standards
  
  GIT:
  - branch: refactor/[component-name]
  - commit incremental changes
  - push when complete
```

---

## AUTONOMOUS TASK EXAMPLES (REAL-WORLD)

### **Example 1: E-commerce Product Catalog**

```bash
& implement product catalog system:
  
  DATABASE:
  - create products table:
    - id (uuid, primary key)
    - name (text, not null)
    - description (text)
    - price (decimal, not null)
    - image_url (text)
    - category (text)
    - stock (integer, default 0)
    - created_at, updated_at (timestamps)
  - add index on category
  - add index on price
  - create RLS policy: anyone can read, only admins can write
  
  API ROUTES:
  - GET /api/products - list products with pagination, filtering by category
  - GET /api/products/[id] - get single product
  - POST /api/products - create product (admin only)
  - PUT /api/products/[id] - update product (admin only)
  - DELETE /api/products/[id] - delete product (admin only)
  - use zod validation for all inputs
  
  PAGES:
  - /app/(shop)/products/page.tsx - product grid with filters
  - /app/(shop)/products/[id]/page.tsx - product detail page
  - /app/(dashboard)/admin/products/page.tsx - admin product management
  
  COMPONENTS:
  - ProductCard - displays product with image, name, price, "Add to Cart" button
  - ProductGrid - responsive grid layout (1 col mobile, 3 cols tablet, 4 cols desktop)
  - ProductFilters - filter by category, price range
  - ProductForm - admin form for creating/editing products
  
  FEATURES:
  - category filtering (Electronics, Clothing, Home, etc.)
  - price range filtering
  - search by product name
  - pagination (12 products per page)
  - sort by: price (low to high), price (high to low), newest
  
  STYLING:
  - use Tailwind CSS
  - product cards with hover effects
  - responsive images
  - clean, modern e-commerce design
  
  QUALITY:
  - follow CLAUDE.md standards
  - error handling for API failures
  - loading skeletons while fetching
  - empty states when no products
  
  GIT:
  - branch: feature/product-catalog
  - commit with descriptive messages
  - push to GitHub when complete
```

### **Example 2: Real-Time Chat System**

```bash
& implement real-time chat system:
  
  DATABASE:
  - create messages table:
    - id (uuid, primary key)
    - room_id (uuid, references rooms)
    - user_id (uuid, references profiles)
    - content (text, not null)
    - created_at (timestamp)
  - create rooms table:
    - id (uuid, primary key)
    - name (text)
    - created_by (uuid, references profiles)
    - created_at (timestamp)
  - add index on room_id and created_at for messages
  - RLS policies: users can read messages in rooms they're members of
  
  REALTIME SETUP:
  - enable Supabase Realtime on messages table
  - subscribe to INSERT events on messages
  - filter by room_id
  
  API ROUTES:
  - GET /api/rooms - list user's rooms
  - POST /api/rooms - create new room
  - GET /api/messages?room_id=[id] - get messages for room
  - POST /api/messages - send new message
  
  PAGES:
  - /app/(dashboard)/chat/page.tsx - chat interface
  
  COMPONENTS:
  - ChatSidebar - list of rooms
  - MessageList - scrollable message feed, auto-scroll to bottom
  - MessageInput - input field with send button
  - MessageBubble - individual message display (left for others, right for user)
  
  FEATURES:
  - real-time message updates (no refresh needed)
  - typing indicators (optional)
  - message timestamps (e.g., "2 min ago")
  - unread message counts per room
  - create new room modal
  
  STYLING:
  - chat UI similar to Slack/Discord
  - use Tailwind CSS
  - smooth animations for new messages
  - responsive (sidebar collapses on mobile)
  
  QUALITY:
  - handle Realtime connection errors
  - reconnect automatically if disconnected
  - optimistic UI updates (show message immediately, confirm later)
  - follow CLAUDE.md standards
  
  GIT:
  - branch: feature/realtime-chat
  - commit incrementally
  - push when complete
```

### **Example 3: Analytics Dashboard**

```bash
& create analytics dashboard:
  
  DATA AGGREGATION:
  - create /app/api/analytics/stats/route.ts
  - aggregate data from posts, users, activity tables
  - return: total users, total posts, active users (last 30 days), post growth
  
  - create /app/api/analytics/chart-data/route.ts
  - return time-series data for charts
  - data: users per day (last 30 days), posts per day (last 30 days)
  
  VISUALIZATION:
  - install recharts: npm install recharts
  - use recharts for all charts
  
  PAGE:
  - /app/(dashboard)/analytics/page.tsx
  
  LAYOUT:
  - grid of stat cards at top (4 cards)
  - two charts below: LineChart (users over time), BarChart (posts per day)
  - responsive: 2x2 grid on desktop, stacked on mobile
  
  STAT CARDS:
  - Total Users (with % change from last month)
  - Total Posts (with % change from last month)
  - Active Users (last 30 days)
  - Avg Posts per User
  
  CHARTS:
  - LineChart: User growth over last 30 days
    - X-axis: dates
    - Y-axis: cumulative user count
    - blue line, gradient fill
  
  - BarChart: Posts created per day (last 30 days)
    - X-axis: dates
    - Y-axis: post count
    - purple bars
  
  DATA FETCHING:
  - fetch on component mount
  - show loading skeleton while fetching
  - refresh button to reload data
  
  STYLING:
  - use Tailwind CSS
  - shadcn/ui Card components for stat cards
  - clean, professional dashboard design
  - responsive charts (resize with container)
  
  QUALITY:
  - error handling for API failures
  - loading states
  - empty states if no data
  - follow CLAUDE.md standards
  
  GIT:
  - branch: feature/analytics-dashboard
  - commit when complete
```

---

## QUALITY ASSURANCE CHECKLIST

Before autonomous task commits code, verify:

### **Code Quality**
- [ ] TypeScript strict mode passes (no errors)
- [ ] ESLint passes (no warnings)
- [ ] All async operations have try-catch error handling
- [ ] Loading states implemented for async operations
- [ ] Error states displayed to users (not just console.log)
- [ ] All functions have TypeScript return types
- [ ] No `any` types used (use `unknown` with type guards)
- [ ] Components under 200 lines (split if larger)

### **User Experience**
- [ ] Loading indicators shown during data fetching
- [ ] Error messages are user-friendly (not technical stack traces)
- [ ] Forms have validation and error display
- [ ] Buttons show loading state when clicked
- [ ] Mobile responsive (tested at 375px, 768px, 1024px)
- [ ] Accessibility attributes added (aria-labels, semantic HTML)
- [ ] Empty states for lists/tables with no data
- [ ] Success feedback after mutations (toasts, redirects)

### **Security**
- [ ] Environment variables used for secrets (never hardcoded)
- [ ] API routes validate input with zod or similar
- [ ] Authentication checked on protected routes
- [ ] Supabase RLS policies configured correctly
- [ ] No sensitive data logged to console in production
- [ ] CORS configured appropriately
- [ ] Rate limiting implemented (if needed)
- [ ] SQL injection prevented (use parameterized queries)

### **Data & Database**
- [ ] Database queries use proper indexes
- [ ] Foreign key constraints defined
- [ ] RLS policies tested (can't access others' data)
- [ ] Cascade delete behavior configured
- [ ] Default values set where appropriate
- [ ] Timestamps (created_at, updated_at) included
- [ ] Unique constraints where needed

### **Testing**
- [ ] Critical paths have tests
- [ ] API routes tested with various inputs
- [ ] Error cases tested (invalid input, unauthorized, etc.)
- [ ] Edge cases considered (empty states, max limits, etc.)
- [ ] Run `npm run build` succeeds locally

### **Documentation**
- [ ] Complex logic has inline comments
- [ ] README updated if setup steps changed
- [ ] CLAUDE.md updated if new patterns established
- [ ] API routes documented (request/response format)
- [ ] Environment variables added to .env.example

### **Git & Deployment**
- [ ] Descriptive commit messages (not "fix" or "update")
- [ ] Branch follows naming convention (feature/*, fix/*, etc.)
- [ ] Code pushed to GitHub
- [ ] Vercel preview deployment triggered successfully
- [ ] No merge conflicts with base branch
- [ ] .gitignore excludes sensitive files (.env, etc.)

---

## TROUBLESHOOTING AUTONOMOUS TASKS

### **Issue: Task Gets Stuck**

**Symptoms:**
- No progress updates for 30+ minutes
- Session appears frozen in Claude Desktop/Mobile

**Diagnosis:**
1. Open session in Claude Desktop
2. Scroll to last message/action
3. Look for indicators:
   - Waiting for external service response?
   - Unclear instructions causing indecision?
   - Error loop (trying same thing repeatedly)?

**Solutions:**

**If task specification was ambiguous:**
```bash
# Terminate stuck task
# Launch new task with more specific instructions

& [restate task with MORE detail]:
  - be explicit about file locations
  - specify exact component names
  - list all expected behaviors
  - provide example code if needed
```

**If waiting on external service:**
```bash
# Check service status
# If service is down, adjust task:

& skip [problematic integration] for now,
  implement rest of feature,
  add TODO comment for later integration
```

**If error loop:**
```bash
# Review error in session
# Launch new task to fix specific error

& fix error in [branch name]:
  - error: [paste exact error]
  - expected: [describe correct behavior]
  - check: [specific thing to verify]
```

### **Issue: Task Completes but Code Doesn't Work**

**Symptoms:**
- Code pushed to GitHub successfully
- Vercel deployment builds successfully
- But functionality is broken when tested

**Diagnosis:**
1. Test Vercel preview URL
2. Check browser console for errors
3. Check Vercel deployment logs

**Solutions:**

**If runtime error:**
```bash
# Teleport session to local for debugging
claude teleport [session-id]

# Or launch new debugging task
& debug and fix runtime error in [branch]:
  - error in browser console: [paste error]
  - occurs when: [steps to reproduce]
  - expected behavior: [describe]
  - test thoroughly before committing
```

**If logic error (no console errors but wrong behavior):**
```bash
& fix logic issue in [branch]:
  - current behavior: [describe what happens]
  - expected behavior: [describe what should happen]
  - likely issue: [your hypothesis]
  - test all edge cases after fixing
```

**If Vercel build succeeds but runtime fails:**
```bash
# Usually environment variable issue
# Check Vercel dashboard → Settings → Environment Variables
# Make sure all required vars are set for Preview deployments

# Or launch fix task:
& fix environment variable issues:
  - add fallback values for missing env vars
  - log warnings if env vars missing
  - update .env.example with all required vars
```

### **Issue: Wrong Files Modified**

**Symptoms:**
- Claude modified files not related to task
- Unexpected changes in commit

**Diagnosis:**
1. Review commit on GitHub
2. Identify which files should NOT have been touched
3. Check if changes break existing functionality

**Solutions:**

**If minor unrelated changes:**
```bash
# Revert specific files
git checkout [branch] -- path/to/wrong/file.tsx
git commit -m "Revert unintended changes to [file]"
git push origin [branch]
```

**If major wrong changes:**
```bash
# Revert entire commit and relaunch task
git revert [commit-hash]
git push origin [branch]

# Launch new task with EXPLICIT file constraints
& [restate task]:
  FILES TO MODIFY:
  - /app/specific/path/file1.tsx
  - /lib/specific/path/file2.ts
  
  DO NOT MODIFY:
  - any files in /components/ui/
  - any files in /lib/supabase.ts
  - any other files not listed above
```

### **Issue: Task Violates Coding Standards**

**Symptoms:**
- Code doesn't follow CLAUDE.md patterns
- Inconsistent style with rest of project
- Uses anti-patterns

**Solutions:**

**Update CLAUDE.md first:**
```markdown
# Add to CLAUDE.md

## COMMON MISTAKES TO AVOID

### DO NOT:
- Use `any` types in TypeScript
- Create components over 200 lines
- Skip error handling on async operations
- Use inline styles instead of Tailwind
- Hardcode API URLs (use env vars)

### ALWAYS:
- Use Tailwind CSS for styling
- Extract reusable logic to custom hooks
- Include loading and error states
- Test with npm run build before committing
```

**Then launch refactoring task:**
```bash
& refactor [branch] to follow CLAUDE.md standards:
  - fix all TypeScript `any` types
  - add proper error handling to all async operations
  - ensure all components use Tailwind (no inline styles)
  - split components over 200 lines
  - add loading and error states where missing
  - test with npm run build
  - commit only after all standards met
```

### **Issue: Vercel Deployment Fails**

**Symptoms:**
- GitHub push succeeds
- Vercel shows "Failed" status
- Build logs show errors

**Common Causes & Solutions:**

**Build Error (TypeScript/ESLint):**
```bash
# View Vercel logs for specific error
# Fix locally first

git checkout [failing-branch]
npm run build  # Reproduce error locally

# Fix the issues
# Test build succeeds
npm run build

# Commit and push
git add .
git commit -m "Fix build errors: [describe fixes]"
git push origin [branch]
```

**Missing Dependencies:**
```bash
# Vercel log shows: "Cannot find module 'some-package'"

# Add to package.json
npm install some-package

# Commit and push
git add package.json package-lock.json
git commit -m "Add missing dependency: some-package"
git push origin [branch]
```

**Environment Variables Missing:**
```bash
# Vercel dashboard → Settings → Environment Variables
# Add missing variables for Preview deployments

# Common missing vars:
# - NEXT_PUBLIC_SUPABASE_URL
# - NEXT_PUBLIC_SUPABASE_ANON_KEY
# - N8N_WEBHOOK_BASE_URL

# After adding, trigger redeploy:
# Vercel → Deployments → Click failed deployment → "Redeploy"
```

---

## GIT WORKFLOW PATTERNS

### **Basic Feature Workflow**

```bash
# 1. Launch autonomous task (creates branch automatically)
& implement user profile feature

# 2. Claude works autonomously, commits to feature/user-profile

# 3. Review on Vercel preview
# Test at: your-project-git-feature-user-profile.vercel.app

# 4. Merge to staging
git checkout staging
git merge feature/user-profile
git push origin staging

# 5. Test on staging
# Test at: your-project-git-staging.vercel.app

# 6. Merge to production
git checkout main
git merge staging
git push origin main

# 7. Delete feature branch
git branch -d feature/user-profile
git push origin --delete feature/user-profile
```

### **Parallel Features Workflow**

```bash
# 1. Launch multiple autonomous tasks
& implement authentication system  # creates feature/auth
& build dashboard                  # creates feature/dashboard
& create blog system               # creates feature/blog

# 2. All complete independently

# 3. Merge in dependency order
git checkout staging

# First: Foundation (auth - others depend on it)
git merge feature/auth
git push origin staging
# Test authentication on staging

# Second: Independent features
git merge feature/dashboard
git push origin staging
# Test dashboard (should work with auth)

git merge feature/blog
git push origin staging
# Test blog (should work with auth)

# 4. Final staging test (all features together)
# Test full app on staging

# 5. Deploy to production
git checkout main
git merge staging
git push origin main
```

### **Hotfix Workflow**

```bash
# Critical bug in production!

# 1. Create hotfix branch from main
git checkout main
git checkout -b hotfix/critical-payment-bug

# 2. Launch autonomous fix OR fix locally
& fix payment processing bug:
  - error: payments failing with "Invalid token"
  - cause: Stripe API key rotation
  - solution: update to new API key
  - test: process test payment successfully
  - urgent: this is production hotfix

# 3. Test thoroughly locally
npm run build
npm run dev
# Test payment flow multiple times

# 4. Merge to main IMMEDIATELY
git checkout main
git merge hotfix/critical-payment-bug
git push origin main
# Production deploys automatically

# 5. Back-merge to staging
git checkout staging
git merge hotfix/critical-payment-bug
git push origin staging

# 6. Clean up
git branch -d hotfix/critical-payment-bug
```

---

## SECURITY BEST PRACTICES

### **Environment Variables**

**Never commit secrets:**

```bash
# .gitignore (verify these are included)
.env
.env.local
.env.production
.env.development
.env*.local
```

**Always provide template:**

```bash
# .env.example (commit this to repo)
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here

# n8n Webhooks
N8N_WEBHOOK_BASE_URL=https://your-n8n-instance.com
N8N_WELCOME_EMAIL_WEBHOOK=
N8N_PASSWORD_RESET_WEBHOOK=

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
NODE_ENV=development
```

**Validate on startup:**

```typescript
// /lib/env.ts
const requiredEnvVars = [
  'NEXT_PUBLIC_SUPABASE_URL',
  'NEXT_PUBLIC_SUPABASE_ANON_KEY',
  'SUPABASE_SERVICE_ROLE_KEY',
] as const

for (const envVar of requiredEnvVars) {
  if (!process.env[envVar]) {
    throw new Error(`Missing required environment variable: ${envVar}`)
  }
}

// Export typed env vars
export const env = {
  supabase: {
    url: process.env.NEXT_PUBLIC_SUPABASE_URL!,
    anonKey: process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    serviceRoleKey: process.env.SUPABASE_SERVICE_ROLE_KEY!,
  },
  app: {
    url: process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:3000',
  },
} as const
```

### **Input Validation**

```typescript
// Always validate user input with zod

import { z } from 'zod'

const userInputSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
  age: z.number().int().positive().max(120),
  terms: z.boolean().refine((val) => val === true, {
    message: 'You must accept the terms',
  }),
})

export async function POST(request: NextRequest) {
  const body = await request.json()
  
  try {
    const validated = userInputSchema.parse(body)
    // Use validated data - guaranteed to be correct type
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { 
          error: 'Invalid input', 
          details: error.errors.map(e => ({
            field: e.path.join('.'),
            message: e.message,
          })),
        },
        { status: 400 }
      )
    }
  }
}
```

### **Rate Limiting**

```bash
# Install Upstash Redis
npm install @upstash/ratelimit @upstash/redis

# Sign up at upstash.com, create Redis database
# Add to .env.local:
UPSTASH_REDIS_REST_URL=
UPSTASH_REDIS_REST_TOKEN=
```

```typescript
// /lib/rate-limit.ts
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL!,
  token: process.env.UPSTASH_REDIS_REST_TOKEN!,
})

// 10 requests per 10 seconds
export const rateLimiter = new Ratelimit({
  redis,
  limiter: Ratelimit.slidingWindow(10, '10 s'),
  analytics: true,
})

// Use in API routes:
export async function POST(request: NextRequest) {
  const ip = request.ip ?? '127.0.0.1'
  const { success, remaining } = await rateLimiter.limit(ip)
  
  if (!success) {
    return NextResponse.json(
      { error: 'Too many requests. Please try again later.' },
      { 
        status: 429,
        headers: { 'X-RateLimit-Remaining': remaining.toString() },
      }
    )
  }
  
  // Continue with request...
}
```

---

## COST OPTIMIZATION

### **Minimizing Token Usage in Background Tasks**

**Inefficient Task Specification:**
```bash
❌ & build a really nice looking landing page with cool animations 
     and make it look professional and modern
```

Problems:
- Vague requirements cause back-and-forth (wastes tokens)
- Claude explores multiple directions
- Generates code, scraps it, tries again

**Efficient Task Specification:**
```bash
✅ & create landing page:
     - hero: gradient purple-blue, headline "Build Faster", CTA "Get Started"
     - features: grid of 6 items with icons from lucide-react
     - testimonials: carousel, 4 quotes (make up placeholder quotes)
     - footer: links to About, Contact, Terms, Privacy + social icons
     - Tailwind CSS, mobile responsive
     - branch: feature/landing
```

Benefits:
- Clear requirements
- Single implementation path
- Minimal token waste

### **When to Use Extended Thinking**

Extended thinking uses more tokens but produces higher quality results.

**Use Extended Thinking for:**
- Complex architectural decisions
- Security-critical implementations (auth, payments)
- Performance-critical code (large data processing)
- Multi-step logic with edge cases

**Skip Extended Thinking for:**
- Simple UI components
- Straightforward CRUD operations
- Copy changes
- Styling adjustments

---

## FINAL PRINCIPLES

**1. Autonomous First**
Default to background tasks (`&`) for all substantial work (30+ minutes). Launch once, review later.

**2. Parallel by Default**
Launch multiple autonomous tasks simultaneously when features are independent. 5x faster development.

**3. Specify Completely**
Detailed task specifications prevent Claude from getting stuck and wasting tokens. Be explicit about files, components, behaviors.

**4. Mobile Workflow**
Develop and review from anywhere using Claude Mobile. Launch tasks from phone, test previews, merge from phone.

**5. Context Preservation**
Use teleport to maintain full AI context when switching environments. Git checkout only brings code; teleport brings conversation history and reasoning.

**6. Test Previews**
Every branch gets automatic Vercel preview. Test thoroughly before merging. Share preview URLs with team.

**7. Staging Before Production**
Always merge to staging and test before production. Catch integration issues early.

**8. Document as You Go**
Update CLAUDE.md with new patterns learned from autonomous tasks. Better specs = fewer issues.

**9. Trust but Verify**
Autonomous tasks should complete successfully without intervention, but always review code and test functionality before deploying to production.

**10. Optimize for Flow**
The goal is continuous development: launch tasks during downtime (commute, meetings, lunch), review during productive time. Let AI work while you do other things.

---

## AUTONOMOUS DEVELOPMENT SUCCESS METRICS

### **Ideal Autonomous Task**
- ✅ Specified with complete requirements
- ✅ Runs for 1-4 hours without intervention
- ✅ Completes successfully first try
- ✅ Commits clean, working code
- ✅ Deploys functional Vercel preview
- ✅ Requires minimal human corrections
- ✅ Follows all project standards

### **Signs of Poor Task Specification**
- ❌ Claude asks clarifying questions (task stalled)
- ❌ Multiple revisions needed after completion
- ❌ Code violates project standards
- ❌ Wrong files modified
- ❌ Vercel preview deployment broken
- ❌ Missing error handling or edge cases

### **Optimization Loop**

Improve task specifications over time:

1. **Launch autonomous task**
2. **Review completed work**
3. **Identify specification gaps** (what was unclear?)
4. **Update CLAUDE.md** with learned patterns
5. **Launch next task** with improved specification
6. **Repeat**

Over time, CLAUDE.md becomes comprehensive, and autonomous tasks succeed first try more frequently.

---

## MEASURING SUCCESS

### **Development Velocity**

Track these metrics to measure autonomous workflow success:

**Before Autonomous Tasks:**
- Features per week: 2-3
- Time to deploy feature: 2-3 days
- Human coding hours per feature: 8-16 hours

**After Autonomous Tasks:**
- Features per week: 8-12 (4x increase)
- Time to deploy feature: hours to 1 day
- Human coding hours per feature: 1-2 hours (review/testing only)

### **Time Allocation Shift**

**Before:**
- 80% time coding
- 20% time reviewing/testing

**After:**
- 20% time specifying tasks and reviewing
- 80% time doing other work while AI codes autonomously

### **Quality Metrics**

Track quality to ensure autonomous development doesn't sacrifice standards:

- TypeScript strict mode passing: 100%
- Test coverage: ≥70% for critical paths
- Vercel preview success rate: ≥95%
- Production deployment success rate: ≥99%
- Bugs caught in staging vs. production: 90% in staging

---

**END OF PART 3**

**COMPLETE VIBE CODING CUSTOM INSTRUCTIONS v2.0**

These instructions enable autonomous AI-driven development using:
- Claude Code background tasks (`&` prefix)
- Teleport session switching (cloud ↔ local)
- Parallel development workflows
- Mobile development capabilities
- Production-ready code patterns
- Comprehensive quality assurance

**Version:** 2.0  
**Last Updated:** January 21, 2026  
**Key Innovation:** True autonomous execution via background tasks  
**For:** Claude Projects focused on vibe coding development

*This represents the cutting edge of AI-assisted development as of January 2026, leveraging Claude Code's autonomous execution capabilities for maximum development velocity.*
