<script>
    (g => {
      var h, a, k, p = "The Google Maps JavaScript API", c = "google", l = "importLibrary", q = "__ib__", m = document, b = window;
      b = b[c] || (b[c] = {});
      var d = b.maps || (b.maps = {}), r = new Set(), e = new URLSearchParams();
      u = () => h || (h = new Promise(async (f, n) => {
        await (a = m.createElement("script"));
        e.set("libraries", [...r] + "");
        for (k in g) e.set(k.replace(/[A-Z]/g, t => "_" + t[0].toLowerCase()), g[k]);
        e.set("callback", c + ".maps." + q);
        a.src = `https://maps.${c}apis.com/maps/api/js?` + e;
        d[q] = f;
        a.onerror = () => h = n(Error(p + " could not load.")); 
        a.nonce = m.querySelector("script[nonce]")?.nonce || "";
        m.head.append(a);
      }));
      d[l] ? console.warn(p + " only loads once. Ignoring:", g) : d[l] = (f, ...n) => r.add(f) && u().then(() => d[l](f, ...n));
    })({
      key: "AIzaSyDkIiXrH0S1DJq_dQ6qALzjMUUEwolEnGw",
      v: "weekly"
    });
  
    let map;
    let markers = [];
    let windowsOpen = [];
    async function initMap() {
      const { Map } = await google.maps.importLibrary("maps");
      const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  
      map = new Map(document.getElementById("map"), {
        center: { lat: 34.366743, lng: -89.518652 },
        zoom: 12,
        mapId: "9dd514aacb4d086b",  // Your Map ID
      });
      loadInitialProperties('{{properties}}', AdvancedMarkerElement);
  
    }
  
    function loadInitialProperties(properties, AdvancedMarkerElement){
      const properties_items = [
        {% for property in properties %}
        {
          lat: parseFloat("{{ property.latitude }}"),
          lng: parseFloat("{{ property.longitude }}"),
        },
        {% endfor %}
      ];
      addMarkers(properties_items, AdvancedMarkerElement);
  
    } 
  
    function addMarkers(properties, AdvancedMarkerElement){
      properties.forEach(property => {
        const marker = new AdvancedMarkerElement({
          position: new google.maps.LatLng(property.lat, property.lng),
        });
        markers.push(marker)
      })
      for (i = 0; i < markers.length; i++){
          const marker = new AdvancedMarkerElement({
          position: new google.maps.LatLng(markers[i].position.Fg, markers[i].position.Hg),
          map: map
        });
      }
    }
    initMap();
  
  
  </script>