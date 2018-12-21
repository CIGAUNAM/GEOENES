$(function () {
    $("#main").css('height', $(window).height())
    $(window).on("resize", function () {
        $("#main").css('height', $(window).height())
    });

    var bounds = [
        [13.0, -82.0], // Southwest coordinates
        [35.0, -120.0]  // Northeast coordinates
    ];

    var map = L.map('main', {
        minZoom: 5,
        maxZoom: 22,
        maxBounds: bounds,
        zoomControl: false,
        attributionControl: false
    });
    var hash = new L.Hash(map);

    if (!window.location.hash) {
        map.setView(new L.LatLng(20.59698, -103.59609), 5);
    } else {
        myhash = window.location.hash.replace("#", "");
        myhash = myhash.split("/");
        map.setView(new L.LatLng(myhash[1], myhash[2]), myhash[0]);
    }

    satelite = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
        //attribution: '(Vista satelital Google) PAUGZM &copy; <a href="http://www.ciga.unam.mx" target=_blank>CIGA UNAM</a>.',
        maxZoom: 22,
        keepBuffer: 1,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

    calles = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
        //attribution: '(Vista de calles Google) PAUGZM &copy; <a href="http://www.ciga.unam.mx" target=_blank>CIGA UNAM</a>.',
        maxZoom: 22,
        keepBuffer: 1,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

    minimap = new L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
        minZoom: 6,
        maxZoom: 17,
        keepBuffer: 1,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

    satelite.addTo(map);

    var suelos = L.tileLayer.betterWms('http://localhost:8080/geoserver/ENES/ows?', {
        layers: 'ENES:suelos_suelo',
        tiled: true,
        format: 'image/png',
        transparent: true,
        minZoom: 6,
        maxZoom: 22,
    }).addTo(map);

    var baseLayers = {
        "Satelite": satelite,
        "Calles": calles
    };

    var overlays = {
        "Suelos": suelos,
    };

    var controles = L.control.layers(baseLayers, overlays);

    controles.addTo(map);

    L.control.zoom({
        position: 'topright'
    }).addTo(map);

})