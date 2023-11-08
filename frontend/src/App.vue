<template>
  <DataInputPage/>
  <br><br><br><br><br><br><br><br><br><br><br><br>
  <br><br><br><br><br><br><br><br><br><br><br><br>
  <br><br><br><br><br><br><br><br><br><br><br><br>
  <MoodChart/>
  <CalorieIntakeChart/>
</template>

<script>
import DataInputPage from './components/data-input/DataInputPage'
import MoodChart from './components/charts/MoodChart'
import CalorieIntakeChart from './components/charts/CalorieIntakeChart'

export default {
  name: 'App',
  components: {
    DataInputPage,
    MoodChart,
    CalorieIntakeChart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
