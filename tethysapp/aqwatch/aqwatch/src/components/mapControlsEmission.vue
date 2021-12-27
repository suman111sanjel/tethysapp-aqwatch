<template>
  <div class="card-box full-height full-width about-div">
    <div class="pannel-title">
      <h6 class="title-heading">Map Controls
      </h6>
    </div>
    <div class="body-container">
      <el-form ref="form" :model="form" label-width="100%" :inline="getIsInlineFormorNot" size="mini"
               label-position="left">
<!--        <el-form-item label="Region">-->
<!--          <el-select v-model="form.region" placeholder="Select region" class="full-width">-->
<!--            <el-option-->
<!--                v-for="item in data.region"-->
<!--                :key="item.value"-->
<!--                :label="item.label"-->
<!--                :value="item.value">-->
<!--            </el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->

        <el-form-item label="Inventory">
          <el-select v-model="form.inventory" placeholder="Select" @change="updateMapLayer()">
            <el-option
                v-for="item in data.Inventory"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="Pollutants">
          <el-select v-model="form.pollutants" placeholder="Select" @change="updateMapLayer()">
            <el-option
                v-for="item in data.pollutants"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="Sectors">
          <el-select v-model="form.sectors" placeholder="Select" @change="updateMapLayer()">
            <el-option
                v-for="item in data.sectors"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="year">
          <el-select v-model="form.year" placeholder="Select" @change="updateMapLayer()">
            <el-option
                v-for="item in data.year"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item class="submit-btn full-width">
<!--          <el-button type="primary" class="full-width">Get Emission Plot</el-button>-->
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import {dataSelect} from '../utils/data'
import eventHub from "../utils/utils";

export default {
  name: "mapControlsEmission",
  data() {
    return {
      form: {
        region: '',
        pollutants: '',
        periodicity: '',
        year: '',
        sectors: '',
        inventory: ''
      },
      isInlineForm: true,
      data: dataSelect
    }
  }, methods: {
    async onSubmit() {

    },
    getInLineData() {
      return this.isInlineForm
    },
    updateMapLayer() {
      this.$store.state.pollutants = this.form.pollutants;
      this.$store.state.sectors = this.form.sectors;
      this.$store.state.year = this.form.year;
      this.$store.state.inventory = this.form.inventory;
      eventHub.$emit("InventoryChange");
    }
  },
  computed: {
    getIsInlineFormorNot() {
      return this.getInLineData();
    },
  },
  created() {
    this.form.region = this.$store.state.region;
    this.form.pollutants = this.$store.state.pollutants;
    this.form.sectors = this.$store.state.sectors;
    this.form.year = this.$store.state.year;
  },
  mounted() {
    // Generate the chart
    // eslint-disable-next-line no-undef

  },
}
</script>

<style scoped>

</style>