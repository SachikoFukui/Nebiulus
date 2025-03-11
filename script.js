document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("currentYear").textContent = new Date().getFullYear()

    // Działanie na telefon
    const menuBtn = document.querySelector(".menu-btn")
    const navLinks = document.querySelector(".nav-links")
    let menuOpen = false

    menuBtn.addEventListener("click", () => {
      if (!menuOpen) {
        menuBtn.classList.add("open")
        navLinks.classList.add("active")
        menuOpen = true
      } else {
        menuBtn.classList.remove("open")
        navLinks.classList.remove("active")
        menuOpen = false
      }
    })
  const navItems = document.querySelectorAll(".nav-links a")
  navItems.forEach((item) => {
    item.addEventListener("click", () => {
      menuBtn.classList.remove("open")
      navLinks.classList.remove("active")
      menuOpen = false
    })
  })
    const sections = document.querySelectorAll("section")

    function highlightNavItem() {
        const scrollPosition = window.scrollY

        sections.forEach((section) => {
          const sectionTop = section.offsetTop - 100
          const sectionHeight = section.offsetHeight
          const sectionId = section.getAttribute("id")

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
          navItems.forEach((item) => {
            item.classList.remove("active")
            if (item.getAttribute("href") === `#${sectionId}`) {
              item.classList.add("active")
            }
          })
        }
      })
    }

    window.addEventListener("scroll", highlightNavItem)

    // GWIAZDKIIIIIIIIIIIIIIIII
    const starskontener = document.querySelector(".stars-kontener")
    const starCount = 50

    for (let i = 0; i < starCount; i++) {
      const star = document.createElement("div")
      star.classList.add("star")
      star.style.width = `${Math.random() * 2 + 1}px`
      star.style.height = star.style.width
      star.style.top = `${Math.random() * 100}%`
      star.style.left = `${Math.random() * 100}%`
      star.style.opacity = Math.random()
      star.style.animation = `twinkle ${Math.random() * 5 + 5}s linear infinite`
      starskontener.appendChild(star)
    }

    // Zjazd do kotwic
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault()

        const targetId = this.getAttribute("href")
        if (targetId === "#") return

        const targetElement = document.querySelector(targetId)
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: "smooth",
          })
        }
      })
    })
})

// Dodawanie CSS dla gwiazdek
const styleSheet = document.createElement("style")
styleSheet.textContent = `
    .star {
        position: absolute;
        background-color: white;
        border-radius: 50%;
    }
    
    @keyframes twinkle {
        0% {
            opacity: 0;
            transform: translateY(0);
        }
        50% {
            opacity: 0.8;
        }
        100% {
            opacity: 0;
            transform: translateY(-20px);
        }
    }
`
document.head.appendChild(styleSheet)

