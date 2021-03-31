<template>
  <main>
    <div class="calculator">
      <div class="calculator_body">
        <div class="calculator_screen_wrapper">
          <div class="calculator_screen" v-if="isEnabled">
            <p class="calculator_screen_memory" v-if="memory">M</p>
            <p class="calculator_screen_display">{{ display }}</p>
          </div>
          <div class="calculator_screen" v-else>
          </div>
        </div>
        <div class="buttons_container">
          <div class="button_wrapper">
            <button class="button" v-on:click="onOff()">
              <img src="@/assets/svg/off.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click='sign'>
              <img src="@/assets/svg/plus_minus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="sqrt">
              <img src="@/assets/svg/sqrt.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click='percent'>
              <img src="@/assets/svg/percent.svg" alt=""/>

            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="mrc">
              <img src="@/assets/svg/mrc.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="m_minus">
              <img src="@/assets/svg/m_minus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="m_plus">
              <img src="@/assets/svg/m_plus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--minus">
            <button class="button" @click="subtract">
              <img src="@/assets/svg/minus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('7')">
              <img src="@/assets/svg/numbers/7.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('8')">
              <img src="@/assets/svg/numbers/8.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('9')">
              <img src="@/assets/svg/numbers/9.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--multiply">
            <button class="button" @click="multiply">
              <img src="@/assets/svg/multiply.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('4')">
              <img src="@/assets/svg/numbers/4.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('5')">
              <img src="@/assets/svg/numbers/5.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('6')">
              <img src="@/assets/svg/numbers/6.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click='divide'>
              <img src="@/assets/svg/divide.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('1')">
              <img src="@/assets/svg/numbers/1.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('2')">
              <img src="@/assets/svg/numbers/2.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('3')">
              <img src="@/assets/svg/numbers/3.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="append('0')">
              <img src="@/assets/svg/numbers/0.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--dot">
            <button class="button" @click="decimal">
              <img class="scale_0_5" src="@/assets/svg/dot.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button" @click="equal">
              <img class="scale_0_5" src="@/assets/svg/equals.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--plus ">
            <button class="button" @click="add">
              <img class="scale_0_5" src="@/assets/svg/plus.svg" alt=""/>
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
const utils = require('@/utils/helpers')

export default {
  name: "Calculator",
  data: function () {
    return {
      isEnabled: false,
      previous: null,
      display: 0,
      operator: null,
      operatorClicked: false,
      memory: 0,
    };
  },
  methods: {
    onOff: function () {
      this.isEnabled = !this.isEnabled;
      this.clear();
    },
    clear() {
      this.display = 0;
      this.memory = 0;
    },
    mrc() {
      if (this.isEnabled) {
        this.display = this.memory;
        this.memory = 0;
      }
    },
    m_plus() {
      if (this.isEnabled) {
        this.memory += Number(this.display);
      }
    },
    m_minus() {
      if (this.isEnabled) {
        this.memory -= Number(this.display);
      }
    },
    sign() {
      if (this.isEnabled) {
        this.display = utils.roundUp(
            this.display < 0
                ? (this.display = this.display - this.display * 2)
                : (this.display = this.display - this.display * 2)
        );
      }
    },
    percent() {
      if (this.isEnabled) {
        this.display = utils.roundUp(this.display / 100);
      }
    },
    sqrt() {
      if (this.isEnabled) {
        this.display = utils.roundUp(Math.sqrt(this.display));
      }
    },
    append(number) {
      if (this.isEnabled) {

        if (this.operatorClicked === true) {
          this.display = '';
          this.operatorClicked = false;
        }
        this.display =
            this.display === 0
                ? (this.display = number)
                : '' + this.display + number;
      }
    },
    decimal() {
      if (this.isEnabled) {
        if (!this.operatorClicked) {
          if (this.display.indexOf('.') === -1) {
            this.append('.');
          }
        }
      }
    },
    divide() {
      if (this.isEnabled) {
        this.operator = (a, b) => utils.roundUp(a / b);
        this.previous = this.display;
        this.operatorClicked = true;
      }
    },
    multiply() {
      if (this.isEnabled) {
        this.operator = (a, b) => utils.roundUp(a * b);
        this.previous = this.display;
        this.operatorClicked = true;
      }
    },
    subtract() {
      if (this.isEnabled) {
        this.operator = (a, b) => utils.roundUp(a - b);
        this.previous = this.display;
        this.operatorClicked = true;
      }
    },
    add() {
      if (this.isEnabled) {
        this.operator = (a, b) => utils.roundUp(a + b);
        this.previous = this.display;
        this.operatorClicked = true;
      }
    },
    equal() {
      if (this.isEnabled) {
        this.display = this.operator(Number(this.previous), Number(this.display));
        this.previous = null;
        this.operatorClicked = true;
      }
    }
  }
}
</script>

<style lang="sass">
.calculator
  background: linear-gradient(180deg, #2771AA -3.6%, #081925 71.1%)
  max-width: 130px
  padding: 1px
  border-radius: 7px

.calculator_body
  padding-top: 26px
  padding-left: 10px
  padding-right: 10px
  background: linear-gradient(180deg, #4EA4DC 51.6%, #081925 161.2%)
  border-radius: 8px

.calculator_screen_wrapper
  padding: 2px 2px 1px
  height: 27px
  border-radius: 3px
  background: linear-gradient(0deg, #18476B -2.9%, #2771AA 59.3%, #081925 148.8%)

.calculator_screen
  display: flex
  background: #DFE3D8
  height: 27px
  padding-right: 4px
  border-radius: 3px
  font-size: 13px
  text-align: right
  line-height: 27px
  overflow-x: hidden
  padding-left: 5px
  align-items: center

  &_memory
    font-size: 3px
    margin: 0

  &_display
    margin: 0 0 0 auto

.buttons_container
  display: grid
  grid-template-columns: repeat(4, 1fr)
  grid-template-rows: 14px repeat(5, 18px)
  gap: 6px 4px
  padding: 8px 0 9px


.button
  display: block
  border: none
  outline: none
  padding: 5px 3px 4px
  width: 100%
  height: 100%
  border-radius: 1px
  font-size: 4px
  background: linear-gradient(0deg, #4EA4DC -416%, #2BAFDE 401%)
  transition: .3s

  &_wrapper
    padding: 1px
    background: linear-gradient(180deg, #18476B -5.2%, #2771AA 45.84%, #081925 119.3%)
    border-radius: 2px

    &:nth-child(1),
    &:nth-child(2),
    &:nth-child(3),
    &:nth-child(4)
      .button
        padding: 3px 2px 2px

    &--plus
      grid-row: 5/7
      grid-column: 4

    &--dot
      > button
        padding: 7px 1px 2px

    &--minus
      img
        transform: scale(0.4)

    &--multiply
      img
        transform: scale(0.7)

  > img
    width: 100%
    height: 100%

.button:hover
  background: linear-gradient(180deg, #4EA4DC 51.6%, #081925 131.2%)

.button:active
  background: linear-gradient(0deg, #18476B -2.9%, #2771AA 59.3%, #081925 148.8%)

.scale_0_5
  transform: scale(0.5)
</style>
