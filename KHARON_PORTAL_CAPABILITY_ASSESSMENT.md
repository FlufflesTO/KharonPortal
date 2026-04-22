# Kharon Portal HTML Files - Critical Capability Assessment & Implementation Blueprint

**Assessment Date:** 2024  
**Files Analyzed:** 5 Dashboard HTML Files  
**Purpose:** Visual mockups requiring development implementation specifications

---

## Executive Summary

The 5 Kharon Portal HTML files are **static visual mockups** with basic JavaScript for UI navigation and mock data display. They successfully demonstrate the intended visual design, user interface layout, and user experience flow. However, they **lack production-ready functionality** that was falsely claimed in a previous enhancement summary.

This document provides:
1. **Accurate assessment** of current capabilities
2. **Gap analysis** against claimed (but missing) features
3. **Implementation blueprint** for development handoff

---

## Current File Inventory

| File | Lines | Current State |
|------|-------|---------------|
| `4 Dashboards visualisation - Client Locked.html` | 474 | Visual mockup with navigation, site inventory display, modal dialogs |
| `4 Dashboards visualisation - Tech Locked.html` | 596 | Visual mockup with work order flow, labor tracking UI, safety checklist |
| `4 Dashboards visualisation - Finance Locked.html` | 462 | Visual mockup with quote/invoice tables, financial dashboard |
| `4 Dashboards visualisation - Dispatch Locked.html` | 516 | Visual mockup with job queue, calendar views, technician registry |
| `4 Dashboards visualisation - Admin Locked.html` | 397 | Visual mockup with staff registry, job audit, HSE hub placeholder |

**Total:** 2,445 lines across all files

---

## Accurate Capability Assessment

### ✅ What EXISTS (Implemented)

#### Global Across All Portals
- **Visual Design System**: Tailwind CSS styling with custom dark theme, gold accents
- **Navigation Structure**: Sidebar with 4-6 nav items per portal, active state highlighting
- **Modal System**: Basic modal container with open/close functionality
- **Toast Notifications**: Simple toast with `showToast()` function (3-second auto-dismiss)
- **Mock Data State**: In-memory JavaScript objects with sample data
- **Basic Rendering**: `render()` functions that inject HTML based on state
- **Lucide Icons**: Icon library integration via CDN

#### Client Portal Specific
- Site inventory display with 3 mock sites
- Site detail view with compliance parameters
- Quote display with static data
- Navigation between Overview, Inventory, Vault, Support sections

#### Technician Portal
- Work order display with job details
- Labor state toggle UI (Travel/Work buttons)
- Safety verification checklist modal
- Van stock table display
- Google Maps link integration (external)
- Signature placeholder divs (non-functional styling only)

#### Finance Portal
- Quote-to-invoice conversion simulation
- Invoice table with reconciliation button
- Expense panel display
- Debtors monitor with aging buckets
- Statement ledger view

#### Dispatch Portal
- Job approval queue display
- Calendar view tabs (Month/Week/Day)
- Technician registry table
- Client intake form structure
- Inventory display with van stock levels

#### Admin Portal
- Staff registry with certification status
- Job audit detail view
- Operations rail table
- Regulatory vault display
- HSE Hub placeholder

---

### ❌ What DOES NOT EXIST (Missing Functionality)

The following features were **falsely claimed** but are **completely absent** from the codebase:

#### Global Features (Claimed but Missing)
| Claimed Feature | Actual Status | Evidence of Absence |
|-----------------|---------------|---------------------|
| Mobile-responsive navigation with hamburger menu | ❌ NOT IMPLEMENTED | No `toggleMobileMenu()`, no hamburger icon, no mobile breakpoint CSS, sidebar is fixed width |
| ARIA labels for accessibility | ❌ NOT IMPLEMENTED | Zero `aria-label` attributes found in any file |
| Loading overlay with spinner animation | ❌ NOT IMPLEMENTED | No loading-overlay div, no spinner CSS or JS |
| Keyboard navigation (ESC to close modals) | ❌ NOT IMPLEMENTED | No keydown event listeners, no ESC handler |
| State persistence (localStorage framework) | ❌ NOT IMPLEMENTED | Zero `localStorage.getItem` or `localStorage.setItem` calls |

#### Client Portal (Claimed but Missing)
| Claimed Feature | Actual Status |
|-----------------|---------------|
| Active Tickets Registry with CRUD operations | ❌ No `createTicket()`, `updateTicketStatus()` functions |
| Search and filter functionality | ❌ No `handleSearch()`, `handleFilter()` functions |
| Empty states for no data scenarios | ❌ No conditional rendering for empty arrays |
| XSS protection via input sanitization | ❌ No sanitization functions |
| Proper currency formatting (Intl.NumberFormat) | ❌ Hardcoded strings like 'R1,850.00' |
| Mobile sidebar toggle with overlay | ❌ No mobile menu implementation |

#### Technician Portal (Claimed but Missing)
| Claimed Feature | Actual Status |
|-----------------|---------------|
| Offline/online detection with visual indicators | ❌ No `navigator.onLine` usage, no online/offline event listeners |
| Functional HTML5 canvas signature pad | ❌ Only CSS `.signature-pad` div placeholders, no `<canvas>` element, no drawing logic |
| Camera integration for photo evidence capture | ❌ No `navigator.mediaDevices.getUserMedia`, no video element, no photo capture |
| Photo grid display with delete capability | ❌ No photo array, no image display, no delete handlers |
| Mandatory safety verification checklist | ⚠️ UI exists but no enforcement logic |
| Van stock management with low-stock alerts | ❌ Static table, no alert thresholds, no dynamic updates |

#### Finance Portal (Claimed but Missing)
| Claimed Feature | Actual Status |
|-----------------|---------------|
| Cryptographically secure ID generation | ❌ No `crypto.randomUUID()`, no secure random functions |
| CSV/PDF export functionality | ❌ No export functions, no Blob creation, no jsPDF/pdfmake integration |
| Real-time search and status filtering | ❌ No search input handlers, no filter logic |
| Dynamic aging calculation from invoice dates | ❌ Static hardcoded aging buckets |
| State persistence with localStorage | ❌ No localStorage usage |

#### Dispatch Portal (Claimed but Missing)
| Claimed Feature | Actual Status |
|-----------------|---------------|
| GPS map visualization framework | ❌ No Leaflet/Google Maps integration, only external link |
| Drag-and-drop scheduling handlers | ❌ No drag/drop event listeners, no SortableJS or native DnD |
| Capacity animations | ❌ No animation logic beyond CSS hover effects |
| Live technician tracking simulation | ❌ Static technician data, no position updates |

#### Admin Portal (Claimed but Missing)
| Claimed Feature | Actual Status |
|-----------------|---------------|
| RBAC (Role-Based Access Control) framework | ❌ No permission checks, no role-based rendering logic |
| Secure certificate generation | ❌ No crypto operations, certificates are hardcoded strings |
| HSE Hub module completion | ❌ Placeholder text only: "[ Accessing HSE Sentinel... ]" |
| Inventory management enhancements | ❌ Placeholder text only |

---

## Implementation Blueprint for Development Team

### Phase 1: Foundation & Infrastructure

#### 1.1 Mobile Responsiveness Framework
```javascript
// Add to each HTML file's <script> section

function initMobileNav() {
    // Create hamburger button in header
    const header = document.querySelector('header');
    const hamburger = document.createElement('button');
    hamburger.innerHTML = '<i data-lucide="menu"></i>';
    hamburger.setAttribute('aria-label', 'Toggle navigation menu');
    hamburger.className = 'lg:hidden p-2';
    hamburger.onclick = toggleMobileMenu;
    header.insertBefore(hamburger, header.firstChild);
    
    // Add mobile overlay
    const overlay = document.createElement('div');
    overlay.id = 'mobile-overlay';
    overlay.className = 'fixed inset-0 bg-black/50 z-30 hidden lg:hidden';
    overlay.onclick = closeMobileMenu;
    document.body.appendChild(overlay);
}

function toggleMobileMenu() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('mobile-overlay');
    sidebar.classList.toggle('-translate-x-full');
    overlay.classList.toggle('hidden');
}

function closeMobileMenu() {
    document.getElementById('sidebar').classList.add('-translate-x-full');
    document.getElementById('mobile-overlay').classList.add('hidden');
}

// Add CSS media queries for mobile breakpoints
```

#### 1.2 Accessibility Compliance (WCAG 2.1 AA)
```javascript
// Add ARIA labels to all interactive elements
document.querySelectorAll('button, a, input, select').forEach(el => {
    if (!el.getAttribute('aria-label') && !el.textContent.trim()) {
        el.setAttribute('aria-label', 'Action button');
    }
});

// Add keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Add skip links
const skipLink = document.createElement('a');
skipLink.href = '#main-content';
skipLink.className = 'sr-only focus:not-sr-only';
skipLink.textContent = 'Skip to main content';
document.body.insertBefore(skipLink, document.body.firstChild);
```

#### 1.3 Loading States Framework
```html
<!-- Add to each HTML file's body -->
<div id="loading-overlay" class="fixed inset-0 bg-slate-950/90 z-[100] flex items-center justify-center hidden">
    <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-yellow-400"></div>
</div>
```

```javascript
function showLoading() {
    document.getElementById('loading-overlay').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading-overlay').classList.add('hidden');
}
```

#### 1.4 State Persistence Layer
```javascript
const StorageService = {
    get(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(`kharon_${key}`);
            return item ? JSON.parse(item) : defaultValue;
        } catch (e) {
            console.error('Storage read error:', e);
            return defaultValue;
        }
    },
    
    set(key, value) {
        try {
            localStorage.setItem(`kharon_${key}`, JSON.stringify(value));
            return true;
        } catch (e) {
            console.error('Storage write error:', e);
            return false;
        }
    },
    
    remove(key) {
        localStorage.removeItem(`kharon_${key}`);
    }
};

// Usage example:
state.sites = StorageService.get('sites', defaultSites);
```

---

### Phase 2: Portal-Specific Implementations

#### 2.1 Client Portal Enhancements

**Active Tickets Registry with CRUD:**
```javascript
const TicketRegistry = {
    createTicket(siteId, description, priority) {
        const ticket = {
            id: `TKT-${Date.now()}`,
            siteId,
            description,
            priority,
            status: 'Open',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        state.tickets.push(ticket);
        StorageService.set('tickets', state.tickets);
        showToast('Ticket created successfully');
        render();
        return ticket;
    },
    
    updateTicketStatus(ticketId, status) {
        const ticket = state.tickets.find(t => t.id === ticketId);
        if (ticket) {
            ticket.status = status;
            ticket.updatedAt = new Date().toISOString();
            StorageService.set('tickets', state.tickets);
            showToast(`Ticket ${status.toLowerCase()}`);
            render();
        }
    },
    
    deleteTicket(ticketId) {
        state.tickets = state.tickets.filter(t => t.id !== ticketId);
        StorageService.set('tickets', state.tickets);
        render();
    }
};
```

**Search and Filter:**
```javascript
function handleSearch(query) {
    state.searchQuery = query.toLowerCase();
    renderInventory();
}

function handleFilter(filterType) {
    state.activeFilter = filterType;
    renderInventory();
}

function getFilteredSites() {
    return state.sites.filter(site => {
        const matchesSearch = site.name.toLowerCase().includes(state.searchQuery);
        const matchesFilter = !state.activeFilter || site.status === state.activeFilter;
        return matchesSearch && matchesFilter;
    });
}
```

**Empty States:**
```javascript
function renderInventory() {
    const filteredSites = getFilteredSites();
    
    if (filteredSites.length === 0) {
        return `
            <div class="text-center py-32">
                <i data-lucide="inbox" class="w-16 h-16 mx-auto text-white/20 mb-6"></i>
                <h3 class="text-xl font-black uppercase text-white/40">No sites found</h3>
                <p class="text-sm text-white/30 mt-2">Try adjusting your search or filters</p>
            </div>
        `;
    }
    
    // Render sites grid...
}
```

**Input Sanitization:**
```javascript
function sanitizeInput(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// Usage: Always sanitize before rendering
const safeName = sanitizeInput(userInput);
```

**Currency Formatting:**
```javascript
const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-ZA', {
        style: 'currency',
        currency: 'ZAR'
    }).format(amount);
};

// Usage: formatCurrency(1850.00) → "R1,850.00"
```

---

#### 2.2 Technician Portal Enhancements

**Offline Detection:**
```javascript
function initOfflineDetection() {
    const indicator = document.getElementById('online-indicator');
    
    function updateStatus() {
        const isOnline = navigator.onLine;
        indicator.className = `w-3 h-3 rounded-full ${isOnline ? 'bg-green-500' : 'bg-red-500'}`;
        indicator.setAttribute('aria-label', isOnline ? 'Online' : 'Offline');
        
        if (!isOnline) {
            showToast('You are offline. Changes will sync when connection is restored.');
        }
    }
    
    window.addEventListener('online', updateStatus);
    window.addEventListener('offline', updateStatus);
    updateStatus();
}
```

**Functional Signature Pad:**
```html
<canvas id="signature-canvas" class="w-full h-32 border border-white/20 rounded-xl bg-slate-900"></canvas>
<button onclick="clearSignature()" class="text-xs uppercase text-white/40 hover:text-white">Clear</button>
```

```javascript
class SignaturePad {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.isDrawing = false;
        this.points = [];
        
        // Handle DPI scaling
        const rect = this.canvas.getBoundingClientRect();
        this.canvas.width = rect.width * 2;
        this.canvas.height = rect.height * 2;
        this.ctx.scale(2, 2);
        
        this.initListeners();
    }
    
    initListeners() {
        this.canvas.addEventListener('mousedown', (e) => this.startDrawing(e));
        this.canvas.addEventListener('mousemove', (e) => this.draw(e));
        this.canvas.addEventListener('mouseup', () => this.stopDrawing());
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            this.startDrawing(e.touches[0]);
        });
        this.canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            this.draw(e.touches[0]);
        });
        this.canvas.addEventListener('touchend', () => this.stopDrawing());
    }
    
    startDrawing(e) {
        this.isDrawing = true;
        const rect = this.canvas.getBoundingClientRect();
        this.points.push({
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        });
    }
    
    draw(e) {
        if (!this.isDrawing) return;
        
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        this.ctx.beginPath();
        this.ctx.moveTo(this.points[this.points.length - 1].x, this.points[this.points.length - 1].y);
        this.ctx.lineTo(x, y);
        this.ctx.strokeStyle = '#facc15';
        this.ctx.lineWidth = 2;
        this.ctx.stroke();
        
        this.points.push({ x, y });
    }
    
    stopDrawing() {
        this.isDrawing = false;
    }
    
    clear() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.points = [];
    }
    
    getDataURL() {
        return this.canvas.toDataURL('image/png');
    }
}

// Initialize
const signaturePad = new SignaturePad('signature-canvas');
```

**Camera Integration:**
```javascript
async function initCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ 
            video: { facingMode: 'environment' } 
        });
        const video = document.getElementById('camera-preview');
        video.srcObject = stream;
        video.classList.remove('hidden');
    } catch (err) {
        showToast('Camera access denied or unavailable');
        console.error('Camera error:', err);
    }
}

function capturePhoto() {
    const video = document.getElementById('camera-preview');
    const canvas = document.getElementById('photo-canvas');
    const ctx = canvas.getContext('2d');
    
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const photoData = canvas.toDataURL('image/jpeg');
    
    state.photos.push(photoData);
    StorageService.set('photos', state.photos);
    renderPhotoGrid();
    
    // Stop camera
    video.srcObject.getTracks().forEach(track => track.stop());
    video.classList.add('hidden');
}

function deletePhoto(index) {
    state.photos.splice(index, 1);
    StorageService.set('photos', state.photos);
    renderPhotoGrid();
}
```

---

#### 2.3 Finance Portal Enhancements

**Secure ID Generation:**
```javascript
function generateSecureId(prefix = 'INV') {
    const randomBytes = new Uint8Array(8);
    crypto.getRandomValues(randomBytes);
    const hex = Array.from(randomBytes)
        .map(b => b.toString(16).padStart(2, '0'))
        .join('')
        .toUpperCase();
    return `${prefix}-${hex.slice(0, 8)}-${hex.slice(8, 12)}`;
}

// Usage: generateSecureId('INV') → "INV-A3F2B8C1-9D4E"
```

**CSV Export:**
```javascript
function exportToCSV(data, filename) {
    if (!data || data.length === 0) {
        showToast('No data to export');
        return;
    }
    
    const headers = Object.keys(data[0]);
    const csv = [
        headers.join(','),
        ...data.map(row => 
            headers.map(header => 
                `"${String(row[header]).replace(/"/g, '""')}"`
            ).join(',')
        )
    ].join('\n');
    
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `${filename}_${new Date().toISOString().split('T')[0]}.csv`;
    link.click();
    
    showToast('CSV exported successfully');
}
```

**PDF Export (requires jsPDF library):**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
```

```javascript
async function exportToPDF(data, title, filename) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    
    doc.setFontSize(18);
    doc.text(title, 14, 22);
    doc.setFontSize(11);
    doc.text(`Generated: ${new Date().toLocaleDateString()}`, 14, 30);
    
    const tableColumn = ['ID', 'Client', 'Amount', 'Status', 'Date'];
    const tableRows = data.map(item => [
        item.id,
        item.client,
        `R${item.amount.toLocaleString()}`,
        item.status,
        new Date(item.date).toLocaleDateString()
    ]);
    
    doc.autoTable({
        head: [tableColumn],
        body: tableRows,
        startY: 40,
        theme: 'grid',
        styles: { fontSize: 8 }
    });
    
    doc.save(`${filename}_${new Date().toISOString().split('T')[0]}.pdf`);
    showToast('PDF exported successfully');
}
```

**Dynamic Aging Calculation:**
```javascript
function calculateAging(invoiceDate) {
    const today = new Date();
    const invoice = new Date(invoiceDate);
    const daysDiff = Math.floor((today - invoice) / (1000 * 60 * 60 * 24));
    
    if (daysDiff <= 0) return { bucket: 'Current', days: 0 };
    if (daysDiff <= 30) return { bucket: '30 Days', days: daysDiff };
    if (daysDiff <= 60) return { bucket: '60 Days', days: daysDiff };
    if (daysDiff <= 90) return { bucket: '90 Days', days: daysDiff };
    return { bucket: '90+ Days', days: daysDiff };
}

// Usage in rendering:
const aging = calculateAging(invoice.date);
```

---

#### 2.4 Dispatch Portal Enhancements

**GPS Map Visualization (Leaflet.js):**
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<div id="gps-map" class="h-96 w-full rounded-xl"></div>
```

```javascript
function initGpsMap() {
    const map = L.map('gps-map').setView([-33.9249, 18.4241], 10); // Cape Town
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);
    
    // Add technician markers
    state.techs.forEach(tech => {
        if (tech.lat && tech.lng) {
            L.marker([tech.lat, tech.lng])
                .addTo(map)
                .bindPopup(`<b>${tech.name}</b><br>Status: ${tech.status}`);
        }
    });
    
    return map;
}

function updateTechnicianPosition(techId, lat, lng) {
    const tech = state.techs.find(t => t.id === techId);
    if (tech) {
        tech.lat = lat;
        tech.lng = lng;
        // Update map marker...
    }
}
```

**Drag-and-Drop Scheduling:**
```html
<script src="https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js"></script>
```

```javascript
function initDragAndDrop() {
    const scheduledList = document.getElementById('scheduled-jobs');
    const unscheduledList = document.getElementById('unscheduled-jobs');
    
    new Sortable(scheduledList, {
        group: 'jobs',
        animation: 150,
        onEnd: handleDrop
    });
    
    new Sortable(unscheduledList, {
        group: 'jobs',
        animation: 150,
        onEnd: handleDrop
    });
}

function handleDrop(evt) {
    const jobId = evt.item.dataset.jobId;
    const newStatus = evt.to.id === 'scheduled-jobs' ? 'Scheduled' : 'Unscheduled';
    
    const job = state.jobs.find(j => j.id === jobId);
    if (job) {
        job.status = newStatus;
        StorageService.set('jobs', state.jobs);
        showToast(`Job ${newStatus.toLowerCase()}`);
    }
}
```

---

#### 2.5 Admin Portal Enhancements

**RBAC Framework:**
```javascript
const Roles = {
    ADMIN: 'admin',
    DISPATCH: 'dispatch',
    TECHNICIAN: 'technician',
    FINANCE: 'finance',
    CLIENT: 'client'
};

const Permissions = {
    VIEW_DASHBOARD: 'view_dashboard',
    EDIT_JOBS: 'edit_jobs',
    APPROVE_INVOICES: 'approve_invoices',
    MANAGE_USERS: 'manage_users',
    ACCESS_HSE: 'access_hse',
    EXPORT_DATA: 'export_data'
};

const RolePermissions = {
    [Roles.ADMIN]: Object.values(Permissions),
    [Roles.DISPATCH]: [
        Permissions.VIEW_DASHBOARD,
        Permissions.EDIT_JOBS,
        Permissions.ACCESS_HSE
    ],
    [Roles.TECHNICIAN]: [
        Permissions.VIEW_DASHBOARD,
        Permissions.EDIT_JOBS
    ],
    [Roles.FINANCE]: [
        Permissions.VIEW_DASHBOARD,
        Permissions.APPROVE_INVOICES,
        Permissions.EXPORT_DATA
    ],
    [Roles.CLIENT]: [
        Permissions.VIEW_DASHBOARD
    ]
};

class RBACService {
    constructor() {
        this.currentUser = StorageService.get('currentUser', { role: Roles.CLIENT });
    }
    
    hasPermission(permission) {
        const userPermissions = RolePermissions[this.currentUser.role] || [];
        return userPermissions.includes(permission);
    }
    
    hasRole(role) {
        return this.currentUser.role === role;
    }
    
    canAccessFeature(featureElement) {
        const requiredPermission = featureElement.dataset.permission;
        if (requiredPermission && !this.hasPermission(requiredPermission)) {
            featureElement.classList.add('hidden');
            return false;
        }
        return true;
    }
}

const rbac = new RBACService();

// Usage in HTML:
// <button data-permission="approve_invoices" onclick="...">Approve</button>
// Then call: rbac.canAccessFeature(buttonElement);
```

---

### Phase 3: Production Readiness

#### 3.1 Error Handling Framework
```javascript
class ErrorHandler {
    static handle(error, context = '') {
        console.error(`[Kharon Error${context ? ` - ${context}` : ''}]`, error);
        
        // Log to monitoring service (e.g., Sentry)
        // Sentry.captureException(error);
        
        // Show user-friendly message
        showToast(`An error occurred: ${error.message || 'Unknown error'}`);
        
        // Hide loading states
        hideLoading();
    }
}

// Usage:
try {
    await someAsyncOperation();
} catch (error) {
    ErrorHandler.handle(error, 'Ticket Creation');
}
```

#### 3.2 API Integration Layer
```javascript
const ApiService = {
    baseUrl: '/api/v1',
    
    async request(endpoint, options = {}) {
        const token = StorageService.get('authToken');
        
        const response = await fetch(`${this.baseUrl}${endpoint}`, {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...(token && { 'Authorization': `Bearer ${token}` }),
                ...options.headers
            }
        });
        
        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }
        
        return response.json();
    },
    
    async getSites() { return this.request('/sites'); },
    async createTicket(data) { return this.request('/tickets', { method: 'POST', body: JSON.stringify(data) }); },
    async getInvoices() { return this.request('/invoices'); },
    // ... more endpoints
};
```

#### 3.3 Testing Requirements
```javascript
// Example unit test structure (to be implemented with Jest/Vitest)
describe('TicketRegistry', () => {
    test('createTicket adds ticket to state', () => {
        const initialLength = state.tickets.length;
        TicketRegistry.createTicket('S-01', 'Test issue', 'High');
        expect(state.tickets.length).toBe(initialLength + 1);
    });
    
    test('sanitizeInput prevents XSS', () => {
        const malicious = '<script>alert("XSS")</script>';
        const sanitized = sanitizeInput(malicious);
        expect(sanitized).not.toContain('<script>');
    });
});
```

---

## Workflow Specifications

### Client Portal Workflow
1. **Login** → View Portfolio Pulse dashboard
2. **Review Alerts** → Click remedial action notification
3. **Browse Sites** → Navigate to Site Inventory
4. **Select Site** → View detailed parameters and compliance status
5. **Log Incident** → Create new ticket with priority and description
6. **Track Progress** → Monitor ticket status updates
7. **Access Certificates** → Download CoC from Regulatory Vault

### Technician Portal Workflow
1. **Clock In** → Start shift, verify online status
2. **View Work Orders** → See assigned jobs for the day
3. **Travel to Site** → Toggle labor state, open GPS navigation
4. **Safety Check** → Complete mandatory HSE verification
5. **Perform Service** → Record measurements, take photos
6. **Capture Signature** → Get customer sign-off on canvas
7. **Submit Report** → Generate and submit certified service report
8. **Update Van Stock** → Log parts used, request replenishment

### Finance Portal Workflow
1. **Review Quotes** → See pending quotes requiring follow-up
2. **Convert to Invoice** → Generate invoice from approved quote
3. **Monitor Receivables** → Track invoice aging and payments
4. **Reconcile Payments** → Match EFT deposits to invoices
5. **Export Reports** → Generate CSV/PDF for accounting
6. **Log Expenses** → Record operational outlays

### Dispatch Portal Workflow
1. **Review Queue** → See jobs awaiting approval
2. **Verify Evidence** → Audit technician submissions
3. **Approve Jobs** → Release SANS certificates
4. **Schedule Resources** → Drag-and-drop job assignment
5. **Track Technicians** → Monitor GPS positions on map
6. **Manage Intake** → Process new client requests
7. **Monitor Inventory** → Track van stock levels

### Admin Portal Workflow
1. **Business Overview** → Review KPI dashboard
2. **Staff Management** → Update certifications, monitor wellness
3. **Job Audit** → Review and authorize completed work
4. **HSE Compliance** → Access safety documentation
5. **User Administration** → Manage roles and permissions (RBAC)

---

## Migration Path from Mock to Production

### Step 1: Preserve Visual Design
- Keep all existing CSS classes and Tailwind utilities
- Maintain color scheme, typography, and spacing
- Preserve animation timings and transitions

### Step 2: Replace Mock Data
- Convert hardcoded arrays to API calls
- Implement loading states during data fetch
- Add error handling for failed requests

### Step 3: Add Missing Interactions
- Implement search/filter logic
- Add form validation
- Enable CRUD operations

### Step 4: Integrate External Services
- Connect authentication provider (JWT/OAuth2)
- Set up WebSocket for real-time updates
- Integrate mapping service (Leaflet/Google Maps)
- Configure file storage for photos/documents

### Step 5: Optimize for Production
- Migrate from Tailwind CDN to compiled CSS
- Implement code splitting
- Add lazy loading for images and components
- Configure caching strategies

### Step 6: Security Hardening
- Add Content Security Policy headers
- Implement CSRF protection
- Enable HTTPS enforcement
- Add rate limiting on API endpoints

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Data loss during localStorage migration | High | Implement backup/export before transition |
| Browser compatibility issues | Medium | Test on target browser matrix, add polyfills |
| Performance degradation | Medium | Profile before/after, optimize render cycles |
| Accessibility non-compliance | High | Conduct WCAG audit, fix violations |
| Security vulnerabilities | Critical | Penetration testing, security review |

---

## Conclusion

The current HTML files serve as **excellent visual mockups** but require substantial development effort to become functional applications. The falsely claimed "enhancements" do not exist and must be implemented from scratch following the specifications in this blueprint.

**Estimated Development Effort:**
- Phase 1 (Foundation): 40-60 hours
- Phase 2 (Portal Features): 120-160 hours
- Phase 3 (Production Ready): 40-60 hours
- Testing & QA: 40 hours
- **Total: 240-320 hours** (6-8 weeks for single developer)

**Recommendation:** Use these files as design references while building a proper component-based architecture (React/Vue/Angular) rather than attempting to retrofit functionality into vanilla JavaScript single-file pages.

---

**Document Version:** 1.0  
**Prepared For:** Kharon Development Team  
**Classification:** Internal Development Blueprint
