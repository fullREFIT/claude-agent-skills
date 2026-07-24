# VIBE CODING PROJECT BUILDER — CUSTOM INSTRUCTIONS
## Part 2 of 3: Production-Ready Patterns & Implementation

---

## IMPLEMENTATION PATTERNS & CODE EXAMPLES

### **1. PROJECT FOUNDATION**

#### **1.1 Essential Dependencies by Use Case**

**Supabase Integration:**
```bash
npm install @supabase/supabase-js
npm install @supabase/auth-helpers-nextjs  # For Next.js
npm install @supabase/ssr  # For server-side rendering
```

**TypeScript + Next.js Essentials:**
```bash
npm install -D typescript @types/node @types/react @types/react-dom
npm install zod  # Runtime validation and type inference
```

**UI Components (shadcn/ui):**
```bash
# Initialize shadcn/ui
npx shadcn-ui@latest init

# Add commonly used components
npx shadcn-ui@latest add button
npx shadcn-ui@latest add input
npx shadcn-ui@latest add card
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add table
npx shadcn-ui@latest add toast
npx shadcn-ui@latest add form
```

**Testing:**
```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom
npm install -D @testing-library/user-event
npm install -D jsdom  # For DOM testing
```

**Data Visualization:**
```bash
npm install recharts  # For charts and graphs
```

**Additional Utilities:**
```bash
npm install date-fns  # Date manipulation
npm install clsx tailwind-merge  # For className utilities
npm install react-hook-form  # Form management
npm install @hookform/resolvers  # Zod resolver for forms
```

#### **1.2 Supabase Setup & Configuration**

**Create Supabase Project:**

1. Go to **supabase.com**
2. Click **"New project"**
3. Fill in details:
   - Name: your-saas-project
   - Database Password: (save this securely)
   - Region: (choose closest to users)
4. Click **"Create new project"**
5. Wait for provisioning (2-3 minutes)

**Get Credentials:**

1. Go to **Project Settings** (gear icon)
2. Click **API** in sidebar
3. Copy these values:
   - **Project URL**
   - **anon public** key
   - **service_role** key (keep secret, server-side only)

**Add to Environment Variables:**

```bash
# .env.local
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Supabase Client Setup:**

```typescript
// /lib/supabase.ts
import { createClient } from '@supabase/supabase-js'
import type { Database } from '@/types/database'

// Client-side Supabase client
export const supabase = createClient<Database>(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)

// Server-side Supabase client (for API routes, server components)
import { createClient as createServerClient } from '@supabase/supabase-js'

export const supabaseAdmin = createServerClient<Database>(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!,
  {
    auth: {
      autoRefreshToken: false,
      persistSession: false,
    },
  }
)
```

**Database Schema Example:**

Execute this in Supabase SQL Editor (Dashboard → SQL Editor → New query):

```sql
-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Profiles table (extends auth.users)
create table public.profiles (
  id uuid references auth.users on delete cascade primary key,
  username text unique,
  full_name text,
  avatar_url text,
  bio text,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Enable Row Level Security
alter table public.profiles enable row level security;

-- RLS Policies for profiles
create policy "Public profiles viewable by everyone"
  on public.profiles for select
  using ( true );

create policy "Users can insert own profile"
  on public.profiles for insert
  with check ( auth.uid() = id );

create policy "Users can update own profile"
  on public.profiles for update
  using ( auth.uid() = id );

-- Function to auto-create profile on signup
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, full_name, avatar_url)
  values (
    new.id,
    new.raw_user_meta_data->>'full_name',
    new.raw_user_meta_data->>'avatar_url'
  );
  return new;
end;
$$ language plpgsql security definer;

-- Trigger to call function on new user
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Posts table
create table public.posts (
  id uuid default uuid_generate_v4() primary key,
  user_id uuid references public.profiles(id) on delete cascade not null,
  title text not null,
  content text not null,
  published boolean default false,
  slug text unique not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Enable RLS for posts
alter table public.posts enable row level security;

-- RLS Policies for posts
create policy "Published posts viewable by everyone"
  on public.posts for select
  using ( published = true or auth.uid() = user_id );

create policy "Users can create own posts"
  on public.posts for insert
  with check ( auth.uid() = user_id );

create policy "Users can update own posts"
  on public.posts for update
  using ( auth.uid() = user_id );

create policy "Users can delete own posts"
  on public.posts for delete
  using ( auth.uid() = user_id );

-- Indexes for performance
create index posts_user_id_idx on public.posts(user_id);
create index posts_published_idx on public.posts(published);
create index posts_created_at_idx on public.posts(created_at desc);
create index posts_slug_idx on public.posts(slug);

-- Function to update updated_at timestamp
create or replace function public.handle_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

-- Trigger for profiles updated_at
create trigger handle_profiles_updated_at
  before update on public.profiles
  for each row execute procedure public.handle_updated_at();

-- Trigger for posts updated_at
create trigger handle_posts_updated_at
  before update on public.posts
  for each row execute procedure public.handle_updated_at();
```

**Generate TypeScript Types from Schema:**

```bash
# Install Supabase CLI
npm install -D supabase

# Login to Supabase
npx supabase login

# Link to your project
npx supabase link --project-ref your-project-ref

# Generate types
npx supabase gen types typescript --linked > types/database.ts
```

**TypeScript Types (generated):**

```typescript
// /types/database.ts (auto-generated by Supabase CLI)
export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      profiles: {
        Row: {
          id: string
          username: string | null
          full_name: string | null
          avatar_url: string | null
          bio: string | null
          created_at: string
          updated_at: string
        }
        Insert: {
          id: string
          username?: string | null
          full_name?: string | null
          avatar_url?: string | null
          bio?: string | null
          created_at?: string
          updated_at?: string
        }
        Update: {
          id?: string
          username?: string | null
          full_name?: string | null
          avatar_url?: string | null
          bio?: string | null
          created_at?: string
          updated_at?: string
        }
      }
      posts: {
        Row: {
          id: string
          user_id: string
          title: string
          content: string
          published: boolean
          slug: string
          created_at: string
          updated_at: string
        }
        Insert: {
          id?: string
          user_id: string
          title: string
          content: string
          published?: boolean
          slug: string
          created_at?: string
          updated_at?: string
        }
        Update: {
          id?: string
          user_id?: string
          title?: string
          content?: string
          published?: boolean
          slug?: string
          created_at?: string
          updated_at?: string
        }
      }
    }
  }
}
```

---

### **2. AUTHENTICATION IMPLEMENTATION**

#### **2.1 Authentication Utilities**

```typescript
// /lib/auth.ts
import { supabase } from './supabase'
import type { User } from '@supabase/supabase-js'

export async function signUp(
  email: string,
  password: string,
  metadata?: { full_name?: string; avatar_url?: string }
) {
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: metadata,
    },
  })
  
  if (error) throw error
  return data
}

export async function signIn(email: string, password: string) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  })
  
  if (error) throw error
  return data
}

export async function signOut() {
  const { error } = await supabase.auth.signOut()
  if (error) throw error
}

export async function getCurrentUser(): Promise<User | null> {
  const { data: { user }, error } = await supabase.auth.getUser()
  if (error) throw error
  return user
}

export async function resetPassword(email: string) {
  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${window.location.origin}/auth/reset-password`,
  })
  
  if (error) throw error
}

export async function updatePassword(newPassword: string) {
  const { error } = await supabase.auth.updateUser({
    password: newPassword,
  })
  
  if (error) throw error
}

export async function updateProfile(updates: {
  full_name?: string
  avatar_url?: string
}) {
  const { error } = await supabase.auth.updateUser({
    data: updates,
  })
  
  if (error) throw error
}
```

#### **2.2 useAuth Hook**

```typescript
// /hooks/useAuth.ts
import { useState, useEffect } from 'react'
import { User } from '@supabase/supabase-js'
import { supabase } from '@/lib/supabase'
import { signIn, signUp, signOut } from '@/lib/auth'

export function useAuth() {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check active session
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    // Listen for auth changes
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
    })

    return () => subscription.unsubscribe()
  }, [])

  return {
    user,
    loading,
    signIn,
    signUp,
    signOut,
    isAuthenticated: !!user,
  }
}
```

#### **2.3 Protected Route Middleware**

```typescript
// middleware.ts (Next.js 13+ App Router)
import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs'
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import type { Database } from '@/types/database'

export async function middleware(req: NextRequest) {
  const res = NextResponse.next()
  const supabase = createMiddlewareClient<Database>({ req, res })
  
  const {
    data: { session },
  } = await supabase.auth.getSession()
  
  // Protect dashboard routes
  if (req.nextUrl.pathname.startsWith('/dashboard') && !session) {
    return NextResponse.redirect(new URL('/login', req.url))
  }
  
  // Redirect authenticated users away from auth pages
  if (
    (req.nextUrl.pathname.startsWith('/login') ||
      req.nextUrl.pathname.startsWith('/signup')) &&
    session
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.url))
  }
  
  return res
}

export const config = {
  matcher: ['/dashboard/:path*', '/login', '/signup'],
}
```

#### **2.4 Auth Components**

```typescript
// /components/auth/LoginForm.tsx
'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/hooks/useAuth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

export function LoginForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const { signIn } = useAuth()
  const router = useRouter()

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      await signIn(email, password)
      router.push('/dashboard')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="space-y-2">
        <Label htmlFor="email">Email</Label>
        <Input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="you@example.com"
          required
          disabled={loading}
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="password">Password</Label>
        <Input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="••••••••"
          required
          disabled={loading}
        />
      </div>

      {error && (
        <div className="p-3 rounded-md bg-red-50 border border-red-200">
          <p className="text-sm text-red-600">{error}</p>
        </div>
      )}

      <Button type="submit" className="w-full" disabled={loading}>
        {loading ? 'Signing in...' : 'Sign In'}
      </Button>
    </form>
  )
}
```

```typescript
// /components/auth/SignupForm.tsx
'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/hooks/useAuth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

export function SignupForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [fullName, setFullName] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const { signUp } = useAuth()
  const router = useRouter()

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      await signUp(email, password, { full_name: fullName })
      router.push('/dashboard')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="space-y-2">
        <Label htmlFor="fullName">Full Name</Label>
        <Input
          id="fullName"
          type="text"
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          placeholder="John Doe"
          required
          disabled={loading}
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="email">Email</Label>
        <Input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="you@example.com"
          required
          disabled={loading}
        />
      </div>

      <div className="space-y-2">
        <Label htmlFor="password">Password</Label>
        <Input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="••••••••"
          required
          minLength={8}
          disabled={loading}
        />
        <p className="text-xs text-gray-500">
          Password must be at least 8 characters
        </p>
      </div>

      {error && (
        <div className="p-3 rounded-md bg-red-50 border border-red-200">
          <p className="text-sm text-red-600">{error}</p>
        </div>
      )}

      <Button type="submit" className="w-full" disabled={loading}>
        {loading ? 'Creating account...' : 'Sign Up'}
      </Button>
    </form>
  )
}
```

---

### **3. N8N WEBHOOK INTEGRATION**

#### **3.1 n8n Webhook Utilities**

```typescript
// /lib/n8n.ts
interface N8nWebhookPayload {
  [key: string]: any
}

interface N8nResponse {
  success: boolean
  data?: any
  error?: string
}

export async function triggerN8nWebhook(
  webhookUrl: string,
  payload: N8nWebhookPayload
): Promise<N8nResponse> {
  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`)
    }

    const data = await response.json()
    return { success: true, data }
  } catch (error) {
    console.error('n8n webhook error:', error)
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error',
    }
  }
}

// Retry logic for critical workflows
export async function triggerN8nWithRetry(
  webhookUrl: string,
  payload: N8nWebhookPayload,
  maxRetries = 3
): Promise<N8nResponse> {
  let lastError: Error | null = null

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`)
      }

      const data = await response.json()
      return { success: true, data }
    } catch (error) {
      lastError = error as Error
      console.error(`n8n attempt ${attempt}/${maxRetries} failed:`, error)

      if (attempt < maxRetries) {
        // Exponential backoff: 2s, 4s, 8s
        const delay = Math.pow(2, attempt) * 1000
        await new Promise((resolve) => setTimeout(resolve, delay))
      }
    }
  }

  return {
    success: false,
    error: `Failed after ${maxRetries} attempts: ${lastError?.message}`,
  }
}
```

#### **3.2 Common Workflow Integrations**

```typescript
// /lib/workflows/email.ts
import { triggerN8nWebhook, triggerN8nWithRetry } from '@/lib/n8n'

export async function sendWelcomeEmail(userEmail: string, userName: string) {
  return triggerN8nWebhook(process.env.N8N_WELCOME_EMAIL_WEBHOOK!, {
    email: userEmail,
    name: userName,
    timestamp: new Date().toISOString(),
  })
}

export async function sendPasswordResetEmail(
  userEmail: string,
  resetToken: string
) {
  // Use retry for critical password reset emails
  return triggerN8nWithRetry(process.env.N8N_PASSWORD_RESET_WEBHOOK!, {
    email: userEmail,
    resetUrl: `${process.env.NEXT_PUBLIC_APP_URL}/auth/reset-password?token=${resetToken}`,
    timestamp: new Date().toISOString(),
  })
}

export async function sendWeeklyDigest(userId: string, userEmail: string) {
  return triggerN8nWebhook(process.env.N8N_WEEKLY_DIGEST_WEBHOOK!, {
    userId,
    email: userEmail,
    timestamp: new Date().toISOString(),
  })
}
```

```typescript
// /lib/workflows/user-onboarding.ts
import { triggerN8nWebhook } from '@/lib/n8n'

export async function triggerUserOnboarding(
  userId: string,
  userEmail: string,
  userName: string
) {
  return triggerN8nWebhook(process.env.N8N_ONBOARDING_WEBHOOK!, {
    userId,
    email: userEmail,
    name: userName,
    tasks: [
      { action: 'send_welcome_email', delay: 0 },
      { action: 'create_notion_page', delay: 0 },
      { action: 'add_to_mailchimp', delay: 0 },
      { action: 'send_setup_guide', delay: 3600 }, // 1 hour later
      { action: 'schedule_followup', delay: 86400 }, // 24 hours later
    ],
  })
}
```

```typescript
// /lib/workflows/analytics.ts
import { triggerN8nWebhook } from '@/lib/n8n'

export async function trackUserEvent(
  userId: string,
  eventName: string,
  properties: Record<string, any>
) {
  // Fire and forget - don't block on analytics
  triggerN8nWebhook(process.env.N8N_ANALYTICS_WEBHOOK!, {
    userId,
    event: eventName,
    properties,
    timestamp: new Date().toISOString(),
  }).catch((error) => {
    console.error('Analytics tracking failed:', error)
    // Don't throw - analytics failures shouldn't break user flow
  })
}
```

#### **3.3 Using Workflows in API Routes**

```typescript
// /app/api/auth/signup/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { supabase } from '@/lib/supabase'
import { sendWelcomeEmail } from '@/lib/workflows/email'
import { triggerUserOnboarding } from '@/lib/workflows/user-onboarding'
import { trackUserEvent } from '@/lib/workflows/analytics'

export async function POST(request: NextRequest) {
  try {
    const { email, password, full_name } = await request.json()

    // Create user in Supabase
    const { data, error } = await supabase.auth.signUp({
      email,
      password,
      options: {
        data: { full_name },
      },
    })

    if (error) throw error

    // Trigger async workflows (fire and forget)
    // These run in the background, app doesn't wait for them
    sendWelcomeEmail(email, full_name).catch(console.error)
    triggerUserOnboarding(data.user!.id, email, full_name).catch(console.error)
    trackUserEvent(data.user!.id, 'user_signed_up', { email, full_name })

    return NextResponse.json({
      success: true,
      data: { user: data.user },
    })
  } catch (error) {
    return NextResponse.json(
      {
        success: false,
        error: error instanceof Error ? error.message : 'Signup failed',
      },
      { status: 400 }
    )
  }
}
```

---

### **4. API ROUTES & DATA FETCHING**

#### **4.1 API Route Pattern (Next.js App Router)**

```typescript
// /app/api/posts/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { supabase } from '@/lib/supabase'
import { z } from 'zod'

// Validation schema
const createPostSchema = z.object({
  title: z.string().min(1).max(200),
  content: z.string().min(1),
  published: z.boolean().optional().default(false),
})

// GET /api/posts - List posts
export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url)
    const published = searchParams.get('published') === 'true'
    const limit = parseInt(searchParams.get('limit') || '10')
    const offset = parseInt(searchParams.get('offset') || '0')

    let query = supabase
      .from('posts')
      .select('*, profiles(*)', { count: 'exact' })
      .order('created_at', { ascending: false })
      .range(offset, offset + limit - 1)

    if (published) {
      query = query.eq('published', true)
    }

    const { data, error, count } = await query

    if (error) throw error

    return NextResponse.json({
      success: true,
      data,
      pagination: {
        total: count,
        limit,
        offset,
        hasMore: count ? offset + limit < count : false,
      },
    })
  } catch (error) {
    return NextResponse.json(
      {
        success: false,
        error: error instanceof Error ? error.message : 'Failed to fetch posts',
      },
      { status: 500 }
    )
  }
}

// POST /api/posts - Create new post
export async function POST(request: NextRequest) {
  try {
    const body = await request.json()

    // Validate input
    const validatedData = createPostSchema.parse(body)

    // Get current user
    const {
      data: { user },
    } = await supabase.auth.getUser()
    
    if (!user) {
      return NextResponse.json(
        { success: false, error: 'Unauthorized' },
        { status: 401 }
      )
    }

    // Create post
    const { data, error } = await supabase
      .from('posts')
      .insert([
        {
          ...validatedData,
          user_id: user.id,
          slug: generateSlug(validatedData.title),
        },
      ])
      .select('*, profiles(*)')
      .single()

    if (error) throw error

    return NextResponse.json(
      {
        success: true,
        data,
      },
      { status: 201 }
    )
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        {
          success: false,
          error: 'Invalid input',
          details: error.errors,
        },
        { status: 400 }
      )
    }

    return NextResponse.json(
      {
        success: false,
        error: error instanceof Error ? error.message : 'Failed to create post',
      },
      { status: 500 }
    )
  }
}

function generateSlug(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .substring(0, 100)
}
```

#### **4.2 Dynamic Routes**

```typescript
// /app/api/posts/[id]/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { supabase } from '@/lib/supabase'
import { z } from 'zod'

const updatePostSchema = z.object({
  title: z.string().min(1).max(200).optional(),
  content: z.string().min(1).optional(),
  published: z.boolean().optional(),
})

// GET /api/posts/[id] - Get single post
export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const { data, error } = await supabase
      .from('posts')
      .select('*, profiles(*)')
      .eq('id', params.id)
      .single()

    if (error) throw error

    return NextResponse.json({
      success: true,
      data,
    })
  } catch (error) {
    return NextResponse.json(
      {
        success: false,
        error: 'Post not found',
      },
      { status: 404 }
    )
  }
}

// PUT /api/posts/[id] - Update post
export async function PUT(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const body = await request.json()
    const validatedData = updatePostSchema.parse(body)

    // Get current user
    const {
      data: { user },
    } = await supabase.auth.getUser()
    
    if (!user) {
      return NextResponse.json(
        { success: false, error: 'Unauthorized' },
        { status: 401 }
      )
    }

    // Update post (RLS ensures user owns the post)
    const { data, error } = await supabase
      .from('posts')
      .update(validatedData)
      .eq('id', params.id)
      .eq('user_id', user.id)
      .select('*, profiles(*)')
      .single()

    if (error) throw error

    return NextResponse.json({
      success: true,
      data,
    })
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        {
          success: false,
          error: 'Invalid input',
          details: error.errors,
        },
        { status: 400 }
      )
    }

    return NextResponse.json(
      {
        success: false,
        error: error instanceof Error ? error.message : 'Failed to update post',
      },
      { status: 500 }
    )
  }
}

// DELETE /api/posts/[id] - Delete post
export async function DELETE(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    // Get current user
    const {
      data: { user },
    } = await supabase.auth.getUser()
    
    if (!user) {
      return NextResponse.json(
        { success: false, error: 'Unauthorized' },
        { status: 401 }
      )
    }

    const { error } = await supabase
      .from('posts')
      .delete()
      .eq('id', params.id)
      .eq('user_id', user.id)

    if (error) throw error

    return NextResponse.json({
      success: true,
      message: 'Post deleted',
    })
  } catch (error) {
    return NextResponse.json(
      {
        success: false,
        error: error instanceof Error ? error.message : 'Failed to delete post',
      },
      { status: 500 }
    )
  }
}
```

---

**END OF PART 2**

Continue to **Part 3** for:
- Autonomous task specification templates
- Quality assurance checklists
- Troubleshooting guide
- Git workflow patterns
- Security best practices
- Cost optimization strategies
- Testing patterns
