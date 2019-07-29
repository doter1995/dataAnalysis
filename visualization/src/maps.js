import L from './lib/chineseTmsProviders';

let map;

export function initMap(dom) {
  const svgRender = L.svg({ padding: 0.5 });
  map = L.map(dom).setView([34.3, 108.92], 10);
  L.tileLayer
    .chinaProvider('TianDiTu.Terrain.Map', { maxZoom: 18, minZoom: 5 })
    .addTo(map);

  //   L.control.layers(baseLayers, null).addTo(map);
  L.circle([34.3, 108.92], { radius: 50 }).addTo(map);
  map.on('click', function(e) {
    console.log(e);
  });
}
