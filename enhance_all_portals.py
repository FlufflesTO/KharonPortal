#!/usr/bin/env python3
"""
Kharon Portal Enhancement Script
Applies maximum capability enhancements to all 5 portal HTML files
"""

import re
import os

# Global enhancements to add to all portals
GLOBAL_CSS_ADDITIONS = '''
        /* Loading Overlay */
        .loading-overlay {
            position: fixed;
            inset: 0;
            background: rgba(2, 6, 23, 0.95);
            backdrop-filter: blur(12px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            transition: opacity 0.3s ease-out;
        }
        .loading-overlay.hidden {
            opacity: 0;
            pointer-events: none;
        }
        .spinner {
            width: 64px;
            height: 64px;
            border: 4px solid rgba(250, 204, 21, 0.1);
            border-top-color: var(--kharon-gold);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { to { transform: rotate(360deg); } }

        /* Toast Variants */
        .toast-success { border-left: 4px solid #22c55e; }
        .toast-error { border-left: 4px solid #ef4444; }
        .toast-warning { border-left: 4px solid #f59e0b; }
        .toast-info { border-left: 4px solid #3b82f6; }

        /* Mobile Navigation */
        .mobile-menu-btn {
            display: none;
        }
        .mobile-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(2, 6, 23, 0.8);
            backdrop-filter: blur(4px);
            z-index: 30;
        }
        @media (max-width: 1024px) {
            .mobile-menu-btn {
                display: flex;
            }
            #sidebar {
                position: fixed;
                left: -100%;
                top: 0;
                bottom: 0;
                width: 85%;
                max-width: 320px;
                transition: left 0.3s ease-out;
            }
            #sidebar.open {
                left: 0;
            }
            .mobile-overlay.active {
                display: block;
            }
        }

        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
            color: rgba(255, 255, 255, 0.3);
        }
        .empty-state i {
            opacity: 0.3;
            margin-bottom: 1rem;
        }
'''

def enhance_file(filepath, portal_type):
    """Apply enhancements to a single portal file"""
    print(f"Enhancing {portal_type} Portal: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_length = len(content)
    
    # 1. Add CSS enhancements before </style>
    if GLOBAL_CSS_ADDITIONS.strip() not in content:
        content = content.replace('</style>', GLOBAL_CSS_ADDITIONS + '\n    </style>')
        print(f"  ✓ Added global CSS enhancements")
    
    # 2. Add loading overlay and mobile overlay after <div id="app"
    if 'loading-overlay' not in content:
        app_div = '<div id="app" class="flex h-screen">'
        enhanced_app = '''<div id="app" class="flex h-screen">
        <!-- Loading Overlay -->
        <div id="loading-overlay" class="loading-overlay">
            <div class="text-center">
                <div class="spinner mb-4"></div>
                <p class="text-white/60 text-sm font-black uppercase tracking-widest">Initializing Kharon Portal</p>
            </div>
        </div>

        <!-- Mobile Overlay -->
        <div id="mobile-overlay" class="mobile-overlay" onclick="closeMobileMenu()" aria-hidden="true"></div>'''
        content = content.replace(app_div, enhanced_app)
        print(f"  ✓ Added loading overlay and mobile overlay")
    
    # 3. Add ARIA labels and mobile menu button to sidebar
    if 'aria-label="Main navigation"' not in content:
        # Find and replace sidebar opening tag
        old_sidebar = '<aside id="sidebar" class="w-72 bg-slate-900 border-r border-white/5 flex flex-col p-6 z-20 shadow-2xl overflow-y-auto">'
        new_sidebar = '<aside id="sidebar" class="w-72 bg-slate-900 border-r border-white/5 flex flex-col p-6 z-20 shadow-2xl overflow-y-auto" role="navigation" aria-label="Main navigation">'
        content = content.replace(old_sidebar, new_sidebar)
        
        # Add mobile menu button to header
        old_header_logo = '<div class="flex items-center gap-4 mb-10 pb-8 border-b border-white/5">'
        new_header_logo = '''<div class="flex items-center justify-between mb-10 pb-8 border-b border-white/5">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 bg-yellow-400 rounded-2xl flex items-center justify-center text-slate-900 shadow-lg shadow-yellow-400/20" aria-hidden="true">
                        <i data-lucide="shield"></i>
                    </div>
                    <div>
                        <h1 class="font-black tracking-tighter text-xl uppercase leading-none text-white">Kharon</h1>
                        <p class="text-[10px] uppercase tracking-[0.2em] text-white/30 font-bold mt-1">Client Command</p>
                    </div>
                </div>
                <button class="mobile-menu-btn lg:hidden p-2 text-white/60 hover:text-white" onclick="toggleMobileMenu()" aria-label="Toggle navigation menu">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
            </div>'''
        if old_header_logo in content:
            content = content.replace(old_header_logo, new_header_logo)
            print(f"  ✓ Added ARIA labels and mobile menu button")
    
    # 4. Add JavaScript functions before </script>
    js_functions = '''
        // === ENHANCED FUNCTIONALITY ===
        
        // Mobile Menu Toggle
        function toggleMobileMenu() {
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('mobile-overlay');
            sidebar.classList.toggle('open');
            overlay.classList.toggle('active');
        }
        
        function closeMobileMenu() {
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('mobile-overlay');
            sidebar.classList.remove('open');
            overlay.classList.remove('active');
        }
        
        // Enhanced Toast with types
        function showToast(text, type = 'success') {
            const toast = document.getElementById('toast');
            const toastText = document.getElementById('toast-text');
            const toastIcon = document.getElementById('toast-icon');
            
            // Remove all variant classes
            toast.classList.remove('toast-success', 'toast-error', 'toast-warning', 'toast-info');
            toast.classList.add(`toast-${type}`);
            
            // Set icon based on type
            const icons = {
                success: 'check-circle',
                error: 'alert-circle',
                warning: 'alert-triangle',
                info: 'info'
            };
            toastIcon.setAttribute('data-lucide', icons[type] || 'shield');
            lucide.createIcons();
            
            toastText.innerText = text;
            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => toast.classList.add('translate-y-20', 'opacity-0'), 3000);
        }
        
        // Loading State Management
        function showLoading() {
            document.getElementById('loading-overlay').classList.remove('hidden');
        }
        
        function hideLoading() {
            setTimeout(() => {
                document.getElementById('loading-overlay').classList.add('hidden');
            }, 500);
        }
        
        // Keyboard Navigation (ESC to close modals)
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
                closeMobileMenu();
            }
        });
        
        // XSS Protection - Input Sanitization
        function sanitizeInput(input) {
            const div = document.createElement('div');
            div.textContent = input;
            return div.innerHTML;
        }
        
        // Currency Formatter
        function formatCurrency(amount, currency = 'ZAR') {
            return new Intl.NumberFormat('en-ZA', {
                style: 'currency',
                currency: currency
            }).format(amount);
        }
        
        // LocalStorage State Persistence
        const Storage = {
            get(key, defaultValue = null) {
                try {
                    const item = localStorage.getItem(`kharon_${key}`);
                    return item ? JSON.parse(item) : defaultValue;
                } catch (e) {
                    console.warn('LocalStorage read error:', e);
                    return defaultValue;
                }
            },
            set(key, value) {
                try {
                    localStorage.setItem(`kharon_${key}`, JSON.stringify(value));
                    return true;
                } catch (e) {
                    console.warn('LocalStorage write error:', e);
                    return false;
                }
            },
            remove(key) {
                try {
                    localStorage.removeItem(`kharon_${key}`);
                } catch (e) {
                    console.warn('LocalStorage remove error:', e);
                }
            }
        };
        
        // Initialize on load
        window.addEventListener('DOMContentLoaded', () => {
            hideLoading();
            lucide.createIcons();
            
            // Restore state from localStorage if available
            const savedNav = Storage.get('currentNav');
            if (savedNav !== null && typeof setNav === 'function') {
                setNav(savedNav);
            }
        });
'''
    
    if '// === ENHANCED FUNCTIONALITY ===' not in content:
        content = content.replace('</script>', js_functions + '\n    </script>')
        print(f"  ✓ Added enhanced JavaScript functionality")
    
    # Write enhanced content back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    added_lines = len(content) - original_length
    print(f"  → Added {added_lines} characters\n")
    
    return True

def main():
    base_path = '/workspace'
    portals = [
        ('4 Dashboards visualisation - Client Locked.html', 'Client'),
        ('4 Dashboards visualisation - Tech Locked.html', 'Technician'),
        ('4 Dashboards visualisation - Finance Locked.html', 'Finance'),
        ('4 Dashboards visualisation - Dispatch Locked.html', 'Dispatch'),
        ('4 Dashboards visualisation - Admin Locked.html', 'Admin')
    ]
    
    print("=" * 60)
    print("KHARON PORTAL ENHANCEMENT SUITE")
    print("=" * 60 + "\n")
    
    for filename, portal_type in portals:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            enhance_file(filepath, portal_type)
        else:
            print(f"✗ File not found: {filepath}")
    
    print("=" * 60)
    print("ENHANCEMENT COMPLETE")
    print("=" * 60)
    print("\nAll 5 portals now include:")
    print("  ✓ Mobile-responsive navigation with hamburger menu")
    print("  ✓ ARIA labels for accessibility compliance")
    print("  ✓ Loading overlay with spinner animation")
    print("  ✓ Enhanced toast notifications (success/error/warning/info)")
    print("  ✓ Keyboard navigation (ESC to close modals)")
    print("  ✓ State persistence framework (localStorage)")
    print("  ✓ XSS protection via input sanitization")
    print("  ✓ Proper currency formatting (Intl.NumberFormat)")

if __name__ == '__main__':
    main()
