import React, { Component } from 'react';
import { initMap } from "./maps";
import "./Map.scss";

class Map extends Component {
    constructor(props, context) {
        super(props, context);
        this.mapDom = null;
    }
    componentDidMount() {
        initMap(this.mapDom)
    }

    render() {
        return (
            <div ref={ref => this.mapDom = ref} className="map" />
        );
    }
}

export default Map;