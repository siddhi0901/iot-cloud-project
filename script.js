<script>
async function fetchData() {
    const res = await fetch("http://127.0.0.1:5000/data");
    const data = await res.json();

    if (data.length === 0) {
        document.getElementById("data").innerHTML = "No data yet...";
        return;
    }

    let latest = data[data.length - 1];

    document.getElementById("data").innerHTML =
        "Temperature: " + latest.temperature + " °C <br>" +
        "Humidity: " + latest.humidity + " %";
}

setInterval(fetchData, 3000);
fetchData();
</script>