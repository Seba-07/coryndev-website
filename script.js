// Interactive Process Walkthrough (proceso.html)
const walkthroughEl = document.getElementById('walkthrough');
if (walkthroughEl) {
    const steps = [
        {
            num: '01',
            badge: 'Paso 1',
            title: 'Diagnóstico Sin Costo',
            desc: 'Una reunión de 1 hora donde entendemos tu operación, tus desafíos y qué necesitas para crecer. Sin presupuesto, sin presión. Si no te convencemos, no pasa nada.',
            image: 'proceso1.png',
            alt: 'Reunión de diagnóstico',
            speech: '¡Empecemos conociéndonos! 👋'
        },
        {
            num: '02',
            badge: 'Paso 2',
            title: 'Propuesta con Prototipo',
            desc: 'En ~7 días recibes mockups navegables (no PDFs aburridos). Tocas, clickeas y ves cómo funcionará tu software antes de que escribamos una línea de código.',
            image: 'proceso2.png',
            alt: 'Prototipo navegable',
            speech: '¿Y si lo ves antes de comprometerte? 🎨'
        },
        {
            num: '03',
            badge: 'Paso 3',
            title: 'Desarrollo en Sprints con Demos',
            desc: 'Cada 2 semanas nos juntamos y ves el avance real. Sin sorpresas, sin entregables misteriosos al final. Tu feedback moldea el producto mientras se construye.',
            image: 'proceso3.png',
            alt: 'Sprints con demos',
            speech: 'Transparencia total cada 2 semanas ⚡'
        },
        {
            num: '04',
            badge: 'Paso 4',
            title: 'Entrega + Capacitación',
            desc: 'No te damos "el software y chao". Entrenamos a tu equipo, documentamos los procesos y nos aseguramos de que todos sepan usarlo desde el día 1.',
            image: 'proceso4.png',
            alt: 'Capacitación del equipo',
            speech: 'No te dejamos solo 🎓'
        },
        {
            num: '05',
            badge: 'Paso 5',
            title: 'Soporte Mensual Real',
            desc: 'Un humano responde tus dudas, mejoramos contigo mes a mes. Mientras estemos contigo, tu software crece y se adapta a cómo evoluciona tu negocio.',
            image: 'proceso5.png',
            alt: 'Soporte continuo',
            speech: 'Nos quedamos contigo 🤝'
        }
    ];

    const contentEl = document.getElementById('walkthroughContent');
    const speechTextEl = document.getElementById('speechText');
    const speechWrapEl = document.getElementById('walkthroughSpeech');
    const robotWrap = document.getElementById('robotWrap');
    const progressFill = document.getElementById('walkthroughProgress');
    const counter = document.getElementById('walkthroughCounter');
    const dots = document.querySelectorAll('#walkthroughDots .wdot');
    const prevBtn = document.getElementById('walkPrev');
    const nextBtn = document.getElementById('walkNext');
    const nextLabel = document.getElementById('walkNextLabel');

    let currentStep = 0;
    let isAnimating = false;
    let completed = false;

    const renderStep = (idx) => {
        const step = steps[idx];
        contentEl.innerHTML = `
            <div class="walk-step">
                <div class="walk-step-header">
                    <span class="walk-step-number">${step.num}</span>
                    <span class="walk-step-badge">${step.badge}</span>
                </div>
                <h2 class="walk-step-title">${step.title}</h2>
                <p class="walk-step-desc">${step.desc}</p>
                <div class="walk-step-image">
                    <img src="${step.image}" alt="${step.alt}">
                </div>
            </div>
        `;
    };

    const renderCompletion = () => {
        contentEl.innerHTML = `
            <div class="walk-step completion">
                <div class="walk-completion-icon">
                    <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="20 6 9 17 4 12"/>
                    </svg>
                </div>
                <h2 class="walk-step-title">¡Ya conoces nuestro proceso!</h2>
                <p class="walk-step-desc">5 pasos concretos para transformar tu idea en software real. El primero no cuesta nada — agenda tu diagnóstico.</p>
                <a href="contacto.html" class="walk-completion-cta">
                    <span>Agendar Diagnóstico Gratis</span>
                    <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
                        <path d="M4 10h12m0 0l-4-4m4 4l-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </a>
            </div>
        `;
        // Confetti burst
        spawnConfetti();
    };

    const spawnConfetti = () => {
        const colors = ['#2563eb', '#60a5fa', '#93c5fd', '#10b981', '#fbbf24', '#ef4444'];
        for (let i = 0; i < 24; i++) {
            const c = document.createElement('span');
            c.className = 'walk-confetti';
            c.style.left = (Math.random() * 100) + '%';
            c.style.background = colors[Math.floor(Math.random() * colors.length)];
            c.style.animationDelay = (Math.random() * 0.4) + 's';
            c.style.borderRadius = Math.random() > 0.5 ? '50%' : '1px';
            walkthroughEl.querySelector('.walkthrough-stage').appendChild(c);
            setTimeout(() => c.remove(), 2400);
        }
    };

    const updateUI = () => {
        const total = steps.length;
        const completedSteps = completed ? total : currentStep;

        // Progress bar — full if completed, otherwise fraction
        const pct = completed ? 100 : ((currentStep + 1) / total) * 100;
        progressFill.style.width = pct + '%';

        // Counter
        counter.textContent = completed ? '¡Completado!' : `Paso ${currentStep + 1} de ${total}`;

        // Dots
        dots.forEach((d, i) => {
            d.classList.remove('active', 'completed');
            if (completed) {
                d.classList.add('completed');
            } else if (i === currentStep) {
                d.classList.add('active');
            } else if (i < currentStep) {
                d.classList.add('completed');
            }
        });

        // Speech bubble
        if (completed) {
            speechTextEl.textContent = '¡Hagámoslo realidad! 🚀';
        } else {
            speechTextEl.textContent = steps[currentStep].speech;
        }
        // Restart speech animation
        speechWrapEl.style.animation = 'none';
        void speechWrapEl.offsetWidth;
        speechWrapEl.style.animation = '';

        // Robot bounce
        robotWrap.classList.remove('bounce');
        void robotWrap.offsetWidth;
        robotWrap.classList.add('bounce');

        // Nav buttons
        prevBtn.disabled = completed || currentStep === 0;
        if (completed) {
            nextBtn.style.display = 'none';
        } else if (currentStep === steps.length - 1) {
            nextLabel.textContent = '¡Terminar!';
            nextBtn.classList.add('final');
            nextBtn.style.display = '';
        } else {
            nextLabel.textContent = 'Siguiente';
            nextBtn.classList.remove('final');
            nextBtn.style.display = '';
        }
    };

    const goToStep = (idx, goCompletion = false) => {
        if (isAnimating) return;
        isAnimating = true;
        const existing = contentEl.querySelector('.walk-step');
        if (existing) {
            existing.classList.add('exit');
        }
        setTimeout(() => {
            if (goCompletion) {
                completed = true;
                renderCompletion();
            } else {
                completed = false;
                currentStep = idx;
                renderStep(idx);
            }
            updateUI();
            isAnimating = false;
        }, 300);
    };

    // Initial render
    renderStep(0);
    updateUI();

    // Next button
    nextBtn.addEventListener('click', () => {
        if (currentStep < steps.length - 1) {
            goToStep(currentStep + 1);
        } else {
            // reached final step → show completion
            goToStep(null, true);
        }
    });

    // Prev button
    prevBtn.addEventListener('click', () => {
        if (completed) {
            goToStep(steps.length - 1);
        } else if (currentStep > 0) {
            goToStep(currentStep - 1);
        }
    });

    // Dot navigation
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            if (i !== currentStep || completed) goToStep(i);
        });
    });

    // Keyboard arrows
    document.addEventListener('keydown', (e) => {
        // Only when user is on proceso page and not typing in input
        if (document.activeElement?.tagName === 'INPUT' || document.activeElement?.tagName === 'TEXTAREA') return;
        if (e.key === 'ArrowRight') {
            nextBtn.click();
        } else if (e.key === 'ArrowLeft') {
            prevBtn.click();
        }
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Form submission handler (only on contacto.html)
const contactForm = document.getElementById('contactForm');
if (contactForm) contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const submitButton = this.querySelector('button[type="submit"]');
    const originalButtonText = submitButton.textContent;

    // Deshabilitar botón y cambiar texto
    submitButton.disabled = true;
    submitButton.textContent = 'Enviando...';

    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        message: document.getElementById('message').value
    };

    try {
        // URL del backend desplegado en Railway
        const BACKEND_URL = 'https://coryn-backend-production.up.railway.app/api/contact';

        const response = await fetch(BACKEND_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (data.success) {
            alert('¡Gracias por tu interés! Nos pondremos en contacto contigo pronto.');
            this.reset();
        } else {
            alert('Hubo un error al enviar el mensaje. Por favor intenta nuevamente.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Hubo un error al enviar el mensaje. Por favor intenta nuevamente o contáctanos directamente a coryn.software@gmail.com');
    } finally {
        // Rehabilitar botón y restaurar texto
        submitButton.disabled = false;
        submitButton.textContent = originalButtonText;
    }
});

// Add scroll effect to header
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 40) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -80px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Observe all animated elements
document.querySelectorAll('.process-item, .benefit-item, .support-card, .section-header').forEach((element, index) => {
    element.style.opacity = '0';
    element.style.transform = 'translateY(40px)';
    element.style.transition = `opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1) ${index * 0.1}s, transform 0.8s cubic-bezier(0.4, 0, 0.2, 1) ${index * 0.1}s`;
    observer.observe(element);
});

// Floating Mascot — visibility, dialogs, click-to-open chat
const mascot = document.getElementById('mascot');
const chatModal = document.getElementById('chatModal');

if (mascot) {
    const bubble = mascot.querySelector('.mascot-bubble');
    const currentPage = document.body.dataset.page || 'home';

    // Per-page configuration
    const pageConfigs = {
        home: {
            welcome: '<p>¡Hola! Soy el asistente de <strong>CORYN</strong> 👋</p><p>¿En qué puedo ayudarte hoy?</p>',
            firstBubble: null, // use section-based
            hideButtons: [],
            dialogs: {
                services: ['¿Qué hacemos? 🤔', '¡Mira esto! 👀', 'Esto te va a gustar', '¿Te cuento?'],
                projects: ['¡Nuestros proyectos!', 'Mira lo que creamos 🚀', 'Inspírate aquí', '¡Cosas geniales adentro!'],
                why: ['¿Por qué nosotros?', '¡Aquí va la magia! ✨', 'Te va a interesar', 'Lo que nos hace únicos'],
                contact: ['¿Conversamos? 💬', '¡Hablemos de tu idea!', 'Primera reunión gratis 🎉', '¡Estamos aquí!'],
                default: ['¡Hola! 👋', '¿Pregunta?', '¡Aquí estoy!']
            }
        },
        servicios: {
            welcome: '<p>¡Hola! Veo que estás explorando nuestros <strong>servicios</strong> 👋</p><p>¿Te interesa alguno en particular? Puedo ayudarte.</p>',
            firstBubble: '¿Alguno te convence?',
            hideButtons: ['services'], // redundant on servicios.html
            dialogs: {
                services: ['¿Te interesa este servicio?', '¡Pregunta lo que quieras! 💬', 'Te ayudo a elegir'],
                default: ['¿Dudas? 🤔', '¡Aquí estoy para ayudarte!']
            }
        },
        productos: {
            welcome: '<p>¡Hola! Estás viendo nuestros <strong>productos</strong> 👋</p><p>¿Quieres saber más o tienes una idea propia?</p>',
            firstBubble: '¿Te gusta algo? 👀',
            hideButtons: [],
            dialogs: {
                products: ['¿Te gusta? 😊', '¿Tienes una idea similar?', 'Conversemos 💬'],
                projects: ['¿Te gusta? 😊', '¿Tienes una idea similar?', 'Conversemos 💬'],
                default: ['¿Preguntas?', '¡Estoy aquí!']
            }
        },
        proceso: {
            welcome: '<p>¡Hola! Así trabajamos en <strong>CORYN</strong> 👋</p><p>¿Quieres saber más sobre algún paso?</p>',
            firstBubble: '¿Dudas del proceso?',
            hideButtons: [],
            dialogs: {
                process: ['¿Te cuento más?', '¡Cualquier duda!', 'Estoy aquí 👋'],
                benefits: ['¿Por qué así?', 'Lo que nos hace únicos ✨'],
                'pricing-support': ['¿Cómo empezamos?', '¡Hablemos de cotización!'],
                default: ['¿Pregunta?', '¡Aquí estoy!']
            }
        },
        contacto: {
            welcome: '<p>¡Hola! Estamos a un paso de conversar 👋</p><p>Completa el formulario o escríbeme directo por WhatsApp 💬</p>',
            firstBubble: '¡Escríbenos! 💬',
            hideButtons: ['meeting'], // the page itself is for scheduling
            dialogs: {
                contact: ['¡Llena el formulario!', 'O WhatsApp 💬', 'Respondemos rápido 🚀'],
                default: ['¿Dudas?', '¡Estoy aquí!']
            }
        },
        nosotros: {
            welcome: '<p>¡Hola! ¿Ya te <strong>convencimos</strong>? 😄</p><p>Conversemos sobre tu proyecto.</p>',
            firstBubble: '¿Te convencí? 😄',
            hideButtons: [],
            dialogs: {
                why: ['¿Ya te convencí?', '¡Hagámoslo! 🚀', 'Conversemos'],
                comparison: ['Mira la diferencia 👀', '¡Claro, no?', 'Elige bien 💡'],
                default: ['¿Listos? 🚀', '¡Empecemos!']
            }
        }
    };

    const config = pageConfigs[currentPage] || pageConfigs.home;

    // Override welcome message in chat modal
    const chatWelcome = document.getElementById('chatWelcome');
    if (chatWelcome && config.welcome) {
        chatWelcome.innerHTML = config.welcome;
    }

    // Hide redundant action buttons
    if (config.hideButtons && config.hideButtons.length) {
        config.hideButtons.forEach(action => {
            const btn = chatModal?.querySelector(`[data-action="${action}"]`);
            if (btn) btn.style.display = 'none';
        });
    }

    const pickDialog = (category) => {
        const list = (config.dialogs && config.dialogs[category]) || (config.dialogs && config.dialogs.default) || ['¡Hola! 👋'];
        return list[Math.floor(Math.random() * list.length)];
    };

    const shownSections = new Set();
    let bubbleTimer = null;

    const showBubble = (text) => {
        if (!bubble) return;
        bubble.textContent = text;
        bubble.classList.add('show');
        clearTimeout(bubbleTimer);
        bubbleTimer = setTimeout(() => bubble.classList.remove('show'), 4500);
    };

    // Show mascot: on home wait for scroll past hero; on internal pages show after small delay
    let mascotVisible = false;

    const showMascot = () => {
        if (!mascotVisible) {
            mascot.classList.add('visible');
            mascotVisible = true;
            // Show a page-specific first greeting
            if (config.firstBubble) {
                setTimeout(() => showBubble(config.firstBubble), 600);
            }
        }
    };

    if (currentPage === 'home') {
        const firstSectionAfterHero = document.querySelector(
            '.services-horizontal-home, .services, .page-banner'
        );
        if (firstSectionAfterHero) {
            window.addEventListener('scroll', () => {
                const sectionTop = firstSectionAfterHero.getBoundingClientRect().top;
                const shouldShow = sectionTop <= window.innerHeight * 0.5;
                if (shouldShow) {
                    showMascot();
                } else if (mascotVisible) {
                    mascot.classList.remove('visible');
                    mascotVisible = false;
                }
            });
        }
    } else {
        // Internal pages: show mascot after 1.5s delay
        setTimeout(showMascot, 1500);
    }

    // Trigger greet when a new section enters viewport
    const sectionsToWatch = document.querySelectorAll(
        '.services-horizontal-home, .projects-section, .why-choose-home, .home-contact, ' +
        '.services:not(.services-horizontal-home), .products, .process, .benefits, ' +
        '.pricing-support, .testimonials, .contact, .why-coryn-benefits, .comparison'
    );

    const sectionCategory = (el) => {
        if (el.classList.contains('services-horizontal-home') || el.classList.contains('services')) return 'services';
        if (el.classList.contains('projects-section')) return 'projects';
        if (el.classList.contains('products')) return 'products';
        if (el.classList.contains('why-choose-home') || el.classList.contains('why-coryn-benefits')) return 'why';
        if (el.classList.contains('comparison')) return 'comparison';
        if (el.classList.contains('process')) return 'process';
        if (el.classList.contains('pricing-support')) return 'pricing-support';
        if (el.classList.contains('benefits')) return 'benefits';
        if (el.classList.contains('home-contact') || el.classList.contains('contact')) return 'contact';
        return 'default';
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && mascotVisible && !shownSections.has(entry.target)) {
                shownSections.add(entry.target);
                const cat = sectionCategory(entry.target);
                showBubble(pickDialog(cat));
                mascot.classList.remove('waving');
                void mascot.offsetWidth;
                mascot.classList.add('waving');
                setTimeout(() => mascot.classList.remove('waving'), 1100);
            }
        });
    }, { threshold: 0.4 });

    sectionsToWatch.forEach(s => sectionObserver.observe(s));

    // Click mascot → open chat modal
    const openChat = () => {
        if (!chatModal) return;
        chatModal.classList.add('open');
        chatModal.setAttribute('aria-hidden', 'false');
        clearTimeout(bubbleTimer);
        if (bubble) bubble.classList.remove('show');
    };

    mascot.addEventListener('click', openChat);
    mascot.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openChat();
        }
    });
}

// Chat Modal — close, quick actions, form submit
if (chatModal) {
    const chatBody = document.getElementById('chatBody');
    const chatForm = document.getElementById('chatForm');
    const WHATSAPP_NUMBER = '56948780902';

    const closeChat = () => {
        chatModal.classList.remove('open');
        chatModal.setAttribute('aria-hidden', 'true');
    };

    chatModal.querySelectorAll('[data-close]').forEach(el => {
        el.addEventListener('click', closeChat);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && chatModal.classList.contains('open')) closeChat();
    });

    // Append a new bot message (used after actions)
    const addMessage = (text, type = 'bot') => {
        if (!chatBody) return;
        const div = document.createElement('div');
        div.className = `chat-message ${type}`;
        div.innerHTML = `<p>${text}</p>`;
        chatBody.appendChild(div);
        chatBody.scrollTop = chatBody.scrollHeight;
    };

    // Quick action buttons
    chatModal.querySelectorAll('[data-action]').forEach(btn => {
        btn.addEventListener('click', () => {
            const action = btn.dataset.action;
            if (action === 'meeting') {
                addMessage('Perfecto, completa el formulario abajo y te contactamos en menos de 24 horas para agendar.');
                chatForm?.querySelector('input[name="chat-name"]')?.focus();
            } else if (action === 'services') {
                closeChat();
                setTimeout(() => {
                    window.location.href = 'servicios.html';
                }, 300);
            } else if (action === 'whatsapp') {
                const msg = encodeURIComponent('Hola CORYN, vengo desde la web y me gustaría conversar sobre un proyecto.');
                window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`, '_blank');
            }
        });
    });

    // Form submit → reuse contact backend
    if (chatForm) {
        chatForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = chatForm.querySelector('.chat-send');
            const originalText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Enviando...</span>';

            const data = {
                name: chatForm.elements['chat-name'].value,
                email: chatForm.elements['chat-email'].value,
                phone: '',
                message: chatForm.elements['chat-message'].value
            };

            try {
                const resp = await fetch('https://coryn-backend-production.up.railway.app/api/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                const result = await resp.json();
                if (result.success) {
                    addMessage(`¡Gracias ${data.name}! Recibí tu mensaje. Te contactamos en menos de 24 horas. 🙌`);
                    chatForm.reset();
                } else {
                    addMessage('Hubo un problema enviando el mensaje. Intenta por WhatsApp o email por favor.');
                }
            } catch (err) {
                addMessage('No pudimos enviar el mensaje ahora. Prueba WhatsApp o escríbenos a coryn.software@gmail.com');
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            }
        });
    }
}

