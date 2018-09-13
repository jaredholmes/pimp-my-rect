<template lang="html">
  <div>
    <nav-bar-item></nav-bar-item>
    <div class="container row">
      <div v-if="deletedAlert" class="alert alert-secondary alert-deleted" role="alert">
        Rectangle deleted.
        <button @click="deletedAlert = false;" type="button" class="close alert-close" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <h3 class="page-header mx-auto col-12">Gallery</h3>
      <div class="row col-12 col-lg-4 gallery-form-section">
        <h4 @click="toggleFormSelector(showFilter)" id="filter-selector" class="form-selector col-6 c-secondary active">Filter</h4>
        <h4 @click="toggleFormSelector(showFilter)" id="sort-selector" class="form-selector col-6 c-secondary">Sort</h4>
        <div v-show="showFilter" class="col-12 row gallery-form form-group filter-form">
          <label class="col-5" for="width-filter">Max width: </label>
          <input v-model="filteredProperties.maxWidth" max="350" min="5" class="col-7 custom-range" type="range" name="width-filter">
          <label class="col-5" for="height-filter">Max height: </label>
          <input v-model="filteredProperties.maxHeight" max="350" min="5" class="col-7 custom-range" type="range" name="height-filter">
          <label class="col-5" for="border-filter">Max border: </label>
          <input v-model="filteredProperties.maxBorder" max="100" min="0" class="col-7 custom-range" type="range" name="border-filter">
        </div>
        <div v-show="!showFilter" class="col-12 row gallery-form filter-form">
          <label class="col-5" for="sort-by-select">Sort by:</label>
          <select @change="setSortBy($event.target.value)" class="col-7 form-control" id="sort-by-select" name="sort-by-select">
            <option value="date">Date saved</option>
            <option value="width">Width</option>
            <option value="height">Height</option>
            <option value="border">Border</option>
          </select>
          <label class="col-5" for="order-by-select">Order by:</label>
          <select @change="toggleSortOrder(orderAscending)" class="col-7 form-control" name="order-by-select">
            <option value="desc">Descending</option>
            <option value="asc">Ascending</option>
          </select>
        </div>
      </div>
      <div v-if="galleryHasItems" class="col-12 col-lg-6 offset-lg-1 gallery-display-section">
        <div v-for="i, x in filteredData" class="col-4 col-md-3 gallery-item-container">
          <div :style="{ backgroundColor: filteredData[x].background_color }" class="gallery-item hvr-glow" data-toggle="modal" :data-target="'#' + modalIDPrefix + x">
            <div class="quick-details-container row">
              <div class="col-12 rectangle-quick-detail">
                {{ filteredData[x].width }}px x {{ filteredData[x].height }}px
              </div>
              <div class="col-12 rectangle-quick-detail">
                {{ filteredData[x].border_radius }}px
              </div>
              <div class="col-12 rectangle-quick-detail">
                {{ filteredData[x].background_color }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="col-12 col-lg-6 offset-lg-1 gallery-empty-section">
        <h4>No rectangles in your gallery yet! <router-link to="/">Create one</router-link></h4>
      </div>

      <div v-for="i, x in filteredData" class="modal fade" :id="modalIDPrefix + x" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button class="btn modal-close-button ml-auto" type="button" aria-label="close" data-dismiss="modal">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M405 136.798L375.202 107 256 226.202 136.798 107 107 136.798 226.202 256 107 375.202 136.798 405 256 285.798 375.202 405 405 375.202 285.798 256z"/></svg>
              </button>
            </div>
            <div class="modal-body">
              <div class="modal-display-rectangle" :style="{
                width: filteredData[x].width + 'px',
                height: filteredData[x].height + 'px',
                borderRadius: filteredData[x].border_radius + 'px',
                backgroundColor: filteredData[x].background_color
                }">
              </div>
              <div class="modal-rectangle-details">
                <ul class="list-group">
                  <li class="list-group-item"><b>Width:</b> {{ filteredData[x].width }}px</li>
                  <li class="list-group-item"><b>Height:</b> {{ filteredData[x].height }}px</li>
                  <li class="list-group-item"><b>Color:</b> {{ filteredData[x].background_color }}</li>
                  <li class="list-group-item"><b>Border radius:</b> {{ filteredData[x].border_radius }}px</li>
                </ul>
              </div>
            </div>
            <div class="modal-footer">
              <button @click="deleteRect(filteredData[x].id, x)" type="button" class="btn delete-rectangle-button">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBarItem from './NavBarItem.vue';
import api from '../scripts/api';

export default {
  name: 'GalleryPage',
  components: { NavBarItem },
  data() {
    return {
      showFilter: true,
      galleryData: [],
      filteredData: [],
      sortByProp: 'date',
      orderAscending: false,
      galleryHasItems: false,
      filteredProperties: {
        maxWidth: widthMax,
        maxHeight: widthMax,
        maxBorder: widthMax,
      },
      modalIDPrefix: 'gallery-modal-',
      deletedAlert: false,
    }
  },
  watch: {
    // Watch all values of filteredProperties object and filter
    filteredProperties: {
      handler() {
        this.filteredData = this.galleryData.filter(datum => {
          return (
            datum.height <= this.filteredProperties.maxHeight
            && datum.width <= this.filteredProperties.maxWidth
            && datum.border_radius <= this.filteredProperties.maxBorder
          );
        });
      },
      deep: true
    },
  },
  methods: {
    setUpGallery() {
      api.getUserGallery(user)
        .then((response) => {
          this.galleryData = response.data;
          if (this.galleryData != undefined && this.galleryData.length > 0) {
            this.galleryHasItems = true;
          } else {
            this.galleryHasItems = false;
          }
          this.filteredData = this.galleryData;
          this.setSortBy('date');
        });
    },
    // Toggle between sort and filter forms
    toggleFormSelector(input) {
      const filterSelector = document.getElementById('filter-selector');
      const sortSelector = document.getElementById('sort-selector');
      if (input) {
        this.showFilter = false;
        filterSelector.classList.remove('active');
        sortSelector.classList.add('active');
      } else {
        this.showFilter = true;
        filterSelector.classList.add('active');
        sortSelector.classList.remove('active');
      }
    },
    toggleSortOrder(isAscending) {
      const select = document.getElementById('sort-by-select');
      const val = select.options[select.selectedIndex].value;
      if (isAscending) {
        this.orderAscending = false;
      } else {
        this.orderAscending = true;
      }
      this.setSortBy(val);
    },
    setSortBy(value) {
      // Sorts in descending order by default. If 'Ascending' order is
      // selected the array will be reversed.
      value = value.toUpperCase();
      this.filteredData = this.filteredData.sort((a, b) => {
        switch (value) {
          case 'DATE':
            return b.id - a.id;
            break;
          case 'WIDTH':
            return b.width - a.width;
            break;
          case 'HEIGHT':
            return b.height - a.height;
            break;
          case 'BORDER':
            return b.border_radius - a.border_radius;
            break;
          default:
            return b.id - a.id;
            break;
        };
      });

      if (this.orderAscending) {
        this.filteredData = this.filteredData.reverse();
      }
    },
    deleteRect(id, index) {
      const del = confirm("Are you sure you want to delete this rectangle? This cannot be undone.");
      if (del) {
        api.deleteRectangle(id)
          .then((response) => {
            const modalClose = document.getElementsByClassName('modal-close-button');
            for (var i = 0; i < modalClose.length; i++) {
              modalClose[i].click();
            }
            this.deletedAlert = true;
            this.setUpGallery();
          });
      }
    }
  },
  beforeMount() {
    this.setUpGallery();
    this.$root.setTitle('Gallery');
  },
}
</script>

<style scoped lang="sass">
  @import "../stylesheets/styles"

  // Modified snippet from Hover.css
  // https://github.com/IanLunn/Hover
  .hvr-glow
    display: inline-block
    vertical-align: middle
    -webkit-transform: perspective(1px) translateZ(0)
    transform: perspective(1px) translateZ(0)
    box-shadow: 0 0 1px rgba(0, 0, 0, 0)
    -webkit-transition-duration: 0.2s
    transition-duration: 0.2s
    -webkit-transition-property: box-shadow
    transition-property: box-shadow

  .hvr-glow:hover, .hvr-glow:focus, .hvr-glow:active
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.6)
    cursor: pointer
    z-index: 10

  .form-selector
    text-align: center
    font-weight: 400

  .form-selector.active
    color: $text-main-color
    font-weight: 600

  .form-selector:hover
    cursor: pointer

  .form-selector, label, .custom-range
    margin-bottom: $spacing

  .custom-range
    position: relative
    top: 2px

  select
    position: relative
    bottom: 6px

  .gallery-form-section
    margin-top: 0

  .gallery-form
    max-height: 350px
    margin-top: 0
    margin-bottom: $spacing

  .container.row
    padding-bottom: $spacing-b-2

  .gallery-empty-section

    h4
      text-align: center

  .gallery-display-section
    padding-left: 0

  .gallery-item-container
    height: $spacing-b-4
    display: inline-block

  .gallery-item
    width: 120%
    height: 96%
    text-align: center

  .quick-details-container
    position: absolute
    top: 0
    bottom: 0
    width: 100%
    padding-top: 1.3em
    color: rgba(0, 0, 0, 0)
    font-size: 14px

  .quick-details-container:hover
    color: black
    background-color: rgba(255, 255, 255, 0.3)

  .modal-close-button

    svg
      width: 1.5em
      height: 1.5em

  .modal-body
    padding: 0

  .modal-display-rectangle
    margin: $spacing-s-2 auto

  .modal-rectangle-details

    b
      font-weight: 600

  .delete-rectangle-button
    color: #FF0011
    font-weight: 600
    border: 1px solid #FF0011

  .delete-rectangle-button:hover
    color: #FFFFFF
    background-color: #FF0011
    border-color: #FFFFFF

</style>
