<template lang="html">
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bc-main">
      <a href="/" class="navbar-brand"><h1>Pimp My <span class="rect">Rect</span></h1></a>
      <button class="navbar-toggler ml-auto" type="button" data-toggle="collapse" data-target="#mobile-collapse" aria-controls="mobile-collapse" aria-expanded="false" aria-label="Toggle navigation">
        <svg class="menu-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M432 176H80c-8.8 0-16-7.2-16-16s7.2-16 16-16h352c8.8 0 16 7.2 16 16s-7.2 16-16 16zM432 272H80c-8.8 0-16-7.2-16-16s7.2-16 16-16h352c8.8 0 16 7.2 16 16s-7.2 16-16 16zM432 368H80c-8.8 0-16-7.2-16-16s7.2-16 16-16h352c8.8 0 16 7.2 16 16s-7.2 16-16 16z"/></svg>
      </button>
      <div class="collapse navbar-collapse bc-main" id="mobile-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item ml-auto">
            <router-link to="/" class="nav-link c-secondary">Editor</router-link>
          </li>
          <li class="nav-item ml-auto">
            <router-link to="/gallery/" class="nav-link c-secondary">Gallery</router-link>
          </li>
          <li class="nav-item ml-auto">
            <a href="/log-out/" class="nav-link c-secondary">Log Out</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavBarItem',
};
</script>

<style lang="sass">
@import "../stylesheets/styles"

.navbar
  height: $spacing
  margin-bottom: $spacing
  padding-left: 0
  padding-right: 0
  z-index: 100

  @include media-desktop
    padding: 0 $spacing-s-1

.navbar-brand, .navbar-toggler
  position: relative

.rect
  // Use em in order to allow the text and measurements to scale together
  border: 0.1em solid $text-main-color
  padding-right: 1em
  font-weight: 600

  @include media-desktop
    left: 0

.navbar-toggler
  border: none
  padding-left: 0

  @include media-desktop
    right: 0

.nav-link
  font-weight: 600
  margin-right: $spacing-s-4
  color: $secondary-color!important

.nav-link:hover, .router-link-exact-active
  color: $text-main-color!important

.menu-svg
  height: 1.5em
  width: 1.5em

</style>
