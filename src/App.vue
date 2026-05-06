<template>
  <div class="page">
    <header class="topbar">
      <div class="container topbarInner">
        <a class="logo" href="#">BRAND</a>
        <div class="menuHover">
          <button class="menuBtn">MENU</button>
          <div class="menuPanel">
            <div>
              <h5>MAN</h5>
              <a href="#">Accessories</a>
              <a href="#">Bags</a>
              <a href="#">Denim</a>
              <a href="#">T-Shirts</a>
            </div>
            <div>
              <h5>WOMAN</h5>
              <a href="#">Accessories</a>
              <a href="#">Jackets & Coats</a>
              <a href="#">Polos</a>
              <a href="#">T-Shirts</a>
            </div>
            <div>
              <h5>KIDS</h5>
              <a href="#">Accessories</a>
              <a href="#">Jackets & Coats</a>
              <a href="#">Polos</a>
              <a href="#">T-Shirts</a>
            </div>
          </div>
        </div>
        <div class="icons">
          <span class="icon"></span>
          <span class="icon"></span>
          <span class="icon badgeIcon"><i>5</i></span>
        </div>
      </div>
    </header>

    <section class="hero">
      <div class="heroImage"></div>
      <div class="heroTextWrap">
        <div class="heroText">
          <p class="eyebrow">THE BRAND</p>
          <h1>OF LUXERIOUS <span>FASHION</span></h1>
        </div>
      </div>
    </section>

    <section class="features container">
      <article class="featureCard big">
        <h3>30% OFF</h3>
        <p>FOR WOMEN</p>
      </article>
      <article class="featureCard">
        <h3>HOT DEAL</h3>
        <p>FOR MEN</p>
      </article>
      <article class="featureCard">
        <h3>NEW ARRIVALS</h3>
        <p>FOR KIDS</p>
      </article>
      <article class="featureCard wide">
        <h3>LUXERIOUS & TRENDY</h3>
        <p>ACCESORIES</p>
      </article>
    </section>

    <section class="products container">
      <div class="sectionHead">
        <h2>Featured Items</h2>
        <p>Shop for items based on what we featured this week</p>
      </div>
      <div class="grid">
        <article v-for="n in 6" :key="n" class="product">
          <div class="thumb">
            <div class="thumbOverlay">
              <button class="addToCart">Add to Cart</button>
            </div>
          </div>
          <div class="content">
            <h3>ELLERY X M'O CAPSULE</h3>
            <p>
              Known for her sculptural takes on traditional tailoring, Australian arbiter of cool
              Kym Ellery teams up with Moda Operandi.
            </p>
            <strong>$52.00</strong>
          </div>
        </article>
      </div>
      <button class="browse">Browse All Product</button>
    </section>

    <section class="perks">
      <nav class="nav">
        <article>
          <h4>Free Delivery</h4>
          <p>Worldwide delivery on all. Authorit tively morph next-generation innovtion.</p>
        </article>
        <article>
          <h4>Sales & discounts</h4>
          <p>Worldwide delivery on all. Authorit tively morph next-generation innovtion.</p>
        </article>
        <article>
          <h4>Quality assurance</h4>
          <p>Worldwide delivery on all. Authorit tively morph next-generation innovtion.</p>
        </article>
      </nav>
    </section>

    <section class="subscribe">
      <div class="container subscribeInner">
        <div class="quote">
          <p>
            “Vestibulum quis porttitor dui! Quisque viverra nunc mi, a pulvinar purus condimentum”
          </p>
        </div>
        <div class="form">
          <h3>SUBSCRIBE</h3>
          <p>FOR OUR NEWLETTER AND PROMOTION</p>
          <div class="formRow">
            <input type="email" placeholder="Enter Your Email" />
            <button>Subscribe</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
