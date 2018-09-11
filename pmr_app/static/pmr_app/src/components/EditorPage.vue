<template lang="html">
  <div class="">
    <nav-bar-item></nav-bar-item>
    <div class="container row">
      <div v-if="savedAlert" id="saved-alert" class="alert alert-saved" role="alert" :style="{ borderColor: alertBorder }">
        Rectangle saved to <router-link to="/gallery/">gallery</router-link>.
        <button @click="savedAlert = false;" type="button" class="close alert-close" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div v-if="failedAlert" class="alert alert-danger alert-error">
        Oops! The rectangle couldn't be saved. Please try again.
        <button @click="failedAlert = false;" type="button" class="close alert-close" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div v-if="invalidHexAlert" class="alert alert-danger alert-invalid-hex">
        Please ensure the color is a correct hex value.
        <button @click="invalidHexAlert = false;" type="button" class="close alert-close" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <h3 class="page-header mx-auto col-12">Rectangle Editor</h3>
      <div class="col-12 col-lg-6">
        <form class="" action="index.html" method="post">
          <div class="form-group">
            <label class="col-3 col-md-2" for="width-picker">Width:</label>
            <input type="range" class="custom-range col-5 col-md-7" id="width-picker" min="5" :max="maxWidth" name="width-picker" v-model="outputWidth">
            <input type="number" onkeydown="return false;" :max="maxWidth" min="5" maxlength="3" class="number-input form-control col-3 col-md-2" v-model="outputWidth">

            <label class="col-3 col-md-2" for="height-picker">Height:</label>
            <input type="range" class="custom-range col-5 col-md-7" id="height-picker" min="5" :max="maxHeight" name="height-picker" v-model="outputHeight">
            <input type="number" onkeydown="return false;" max="350" min="5" maxlength="3" class="number-input form-control col-3 col-md-2" v-model="outputHeight">

            <label class="col-3 col-md-2" for="border-picker">Border:</label>
            <input type="range" class="custom-range col-5 col-md-7" id="border-picker" min="0" max="100" name="border-picker" v-model="outputBorder">
            <input type="number" onkeydown="return false;" :max="maxWidth" min="1" maxlength="3" class="number-input form-control col-3 col-md-2" v-model="outputBorder">

            <label class="col-2" for="color-picker">Color:</label>
            <input  type="text" class="text-input col-4 col-sm-3" name="color-picker" maxlength="7" v-model="outputColor.hex">
            <color-slider class="col-5 col-sm-6" v-model="outputColor"></color-slider>

            <button type="button" class="col-3 offset-2 offset-sm-3 btn btn-save bc-secondary" @click="saveRectangle">Save</button>
          </div>
        </form>
      </div>
      <div class="col-12 col-lg-6 output-rect-container">
        <div class="output-rect" id="output" :style="{
          width: outputWidth+'px',
          height: outputHeight+'px',
          borderRadius: outputBorder+'px',
          maxWidth: maxWidth + 'px',
          maxHeight: maxHeight + 'px',
          backgroundColor: outputColor.hex
          }">
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import NavBarItem from './NavBarItem.vue';
import api from '../scripts/api.js';
import axios from 'axios';
import { Slider } from 'vue-color';

export default {
  name: 'EditorPage',
  components: {
    NavBarItem,
    'ColorSlider': Slider,
  },
  data() {
    return {
      outputWidth: 263,
      outputHeight: 175,
      outputBorder: 25,
      outputColor: {
        hex: '#FF19A3'
      },
      maxWidth: 350,
      maxHeight: 350,
      savedAlert: false,
      failedAlert: false,
      invalidHexAlert: false,
      alertBorder: '',
    }
  },
  methods: {
    saveRectangle() {
      // TODO: improve hex validation
      if (this.outputColor.hex.length <= 7 && this.outputColor.hex.charAt(0) === '#') {
        api.createRectangle(1, this.outputWidth, this.outputHeight, this.outputBorder, this.outputColor.hex)
          .then((response) => {
            this.savedAlert = true;
            // Seperate variable alertBorder is required, or else the border
            // color changes as the user changes the color in the editor
            this.alertBorder = this.outputColor.hex;
          })
          .catch((response) => {
            this.failedAlert = true;
          });
      } else {
        this.invalidHexAlert = true;
      }
    }
  },
  watch: {
    width() {
      this.con();
    }
  },
  beforeMount() {
    const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    axios.defaults.headers.post['X-CSRFToken'] = csrf;
  }
}
</script>

<style scoped lang="sass">
@import "../stylesheets/styles"

.alert-saved
  background-color: #FFFFFF
  border: 2px solid

form
  width: 100%

.text-input, .number-input
  display: inline
  margin: 0
  margin-bottom: $spacing*3/4
  height: $spacing * 3/4 * 3/4
  border: 1px solid #ced4da

.btn-save
  position: relative
  bottom: 2px
  height: $spacing * 3/4 * 3/4
  color: #FFFFFF
  font-weight: 600

.btn-save:hover
  background-color: #FFFFFF
  border: 1px solid $secondary-color
  color: $secondary-color

.btn-save:active
  background-color: $main-color

.output-rect-container
  height: 490px // 90 * 4(4/3)

.output-rect
  margin: auto

.vc-slider
  display: inline-block
  position: relative
  top: 15px

</style>