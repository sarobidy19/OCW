---
---

{% include js/conference.js %}

window.conference.awaitReady().then(() => {
    const map = window.conference.map.getMap();

    if (typeof map !== 'undefined') {
        let main_venue = L.marker([45.38212053136539, -75.6976344052204], {
            icon: L.divIcon({
                className: '',
                html: '<span class="fa fa-map-marker"></span> Workshop venue',
                iconSize: [10, 6]
            })
        }).addTo(map);
        let main_airport = L.marker([45.31837089019712, -75.66593183332223], {
            icon: L.divIcon({
                className: '',
                html: '<span class="fa fa-plane"></span> YOW Airport',
                iconSize: [10, 6]
            })
        }).addTo(map);
        let main_train_station = L.marker([45.417519486223085, -75.65155234305104], {
            icon: L.divIcon({
                className: '',
                html: '<span class="fa fa-train"></span> Train Station',
                iconSize: [10, 6]
            })
        }).addTo(map);
        let main_residence = L.marker([45.42263409490239, -75.68489838922196], {
            icon: L.divIcon({
                className: '',
                html: '<span class="fa fa-map-marker"></span> 90 Residence University of Ottawa',
                iconSize: [10, 6]
            })
        }).addTo(map);
    }
});



