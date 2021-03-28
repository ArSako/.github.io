<template>
  <main>
    <div class="calculator">
      <div class="calculator_body">
        <div class="calculator_screen_wrapper">
          <div class="calculator_screen"></div>
        </div>
        <div class="buttons_container">
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/off.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/plus_minus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/sqrt.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/percent.svg" alt=""/>

            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/mrc.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/m_minus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/m_plus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--minus">
            <button class="button">
              <img src="@/assets/svg/minus.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/7.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/8.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/9.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--multiply">
            <button class="button">
              <img src="@/assets/svg/multiply.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/4.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/5.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/6.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/divide.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/1.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/2.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/3.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img src="@/assets/svg/numbers/0.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img class="scale_0_5" src="@/assets/svg/dot.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper">
            <button class="button">
              <img class="scale_0_5" src="@/assets/svg/equals.svg" alt=""/>
            </button>
          </div>
          <div class="button_wrapper button_wrapper--plus ">
            <button class="button">
              <img class="scale_0_5" src="@/assets/svg/plus.svg" alt=""/>
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "Calculator"
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
  background: #DFE3D8
  height: 27px
  border-radius: 3px

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

    &--minus
      img
        transform: scale(0.4)
    &--multiply
      img
        transform: scale(0.7)

  > img
    width: 100%
    height: 100%

.scale_0_5
  transform: scale(0.5)
</style>
