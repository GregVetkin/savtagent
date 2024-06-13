document.addEventListener('DOMContentLoaded', () => {
    const apiEndpoint = 'http://127.0.0.1:8081/storage';
    let previousData = {};

    const fetchData = async () => {
        try {
            const response = await fetch(apiEndpoint);
            if (response.ok) {
                const data = await response.json();
                updateUI(data);
            } else {
                console.error('Failed to fetch data:', response.statusText);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const updateUI = (data) => {
        const container = document.getElementById('disk-info');
        container.innerHTML = ''; // Clear previous data

        data.forEach((disk) => {
            const { device, mountpoint, usage, io } = disk;
            const previousIO = previousData[device]?.io || { read_count: 0, write_count: 0, read_bytes: 0, write_bytes: 0 };

            const diskDiv = document.createElement('div');
            diskDiv.className = 'disk';

            const barColor = getBarColor(usage.percent);

            diskDiv.innerHTML = `
                <div class="disk-info">
                    <h3>${device} (${mountpoint})</h3>
                    <p>Used: ${formatBytes(usage.used)} / ${formatBytes(usage.total)}</p>
                    <div class="bar">
                        <div>
                            <span style="width: ${usage.percent}%; background-color: ${barColor};"></span>
                        </div>
                        <p>${usage.percent}%</p>
                    </div>
                    <p>Reads: ${io.read_count - previousIO.read_count} (${formatBytes(io.read_bytes - previousIO.read_bytes)})</p>
                    <p>Writes: ${io.write_count - previousIO.write_count} (${formatBytes(io.write_bytes - previousIO.write_bytes)})</p>
                </div>
            `;

            container.appendChild(diskDiv);

            previousData[device] = disk;
        });
    };

    const getBarColor = (percent) => {
        if (percent < 70) return '#4caf50'; // green
        if (percent < 90) return '#ffeb3b'; // Yellow
        return '#f44336'; // Red
    };

    const formatBytes = (bytes, decimals = 2) => {
        if (bytes === 0) return '0 B';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    };

    // Fetch data every second
    setInterval(fetchData, 1000);
    fetchData();
});
