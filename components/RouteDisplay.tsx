import React, { useState } from 'react';
import { OptimizedStop, RouteSummary } from '../types';
import { ClockIcon, MapPinIcon, TruckIcon, ClipboardIcon, MapIcon } from './icons';

interface RouteDisplayProps {
  route: OptimizedStop[];
  summary: RouteSummary;
  startPoint: string;
}

const RouteSummaryCard: React.FC<{ summary: RouteSummary }> = ({ summary }) => (
    <div className="bg-gray-700/50 p-4 rounded-lg border border-gray-600 mb-6 flex justify-around items-center">
        <div className="text-center">
            <div className="flex items-center justify-center gap-2">
                <TruckIcon className="w-6 h-6 text-yellow-300" />
                <span className="text-3xl font-bold text-white">{summary.totalStops}</span>
            </div>
            <p className="text-sm text-gray-400">Total de Paradas</p>
        </div>
        <div className="w-px h-12 bg-gray-600"></div>
        <div className="text-center">
            <div className="flex items-center justify-center gap-2">
                <ClockIcon className="w-6 h-6 text-yellow-300" />
                <span className="text-3xl font-bold text-white">{summary.totalTime}</span>
            </div>
             <p className="text-sm text-gray-400">Tempo Total Estimado</p>
        </div>
    </div>
);


const RouteDisplay: React.FC<RouteDisplayProps> = ({ route, summary, startPoint }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    const routeText = `Rota Otimizada Sabor Express\n\n` +
      `Resumo da Rota:\n` +
      `- Total de Paradas: ${summary.totalStops}\n` +
      `- Tempo Total Estimado: ${summary.totalTime}\n\n` +
      `Sequência de Entregas:\n` +
      route.map(stop => `${stop.order}. ${stop.address} (~${stop.estimatedTime} de viagem)`).join('\n');
    
    navigator.clipboard.writeText(routeText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleOpenInMaps = () => {
    if (!route || route.length === 0) return;

    const baseUrl = 'https://www.google.com/maps/dir/';
    
    // Create the full list of waypoints for the URL
    const waypoints = [...route].sort((a, b) => a.order - b.order).map(stop => stop.address);

    // If a custom start point is provided, it becomes the origin.
    if (startPoint && startPoint.trim() !== '') {
        waypoints.unshift(startPoint);
    }
    
    // URL-encode each part of the address and join them with slashes
    const encodedWaypoints = waypoints.map(addr => encodeURIComponent(addr));
    const mapsUrl = `${baseUrl}${encodedWaypoints.join('/')}?travelmode=motorcycle`;

    // Open the generated URL in a new tab
    window.open(mapsUrl, '_blank', 'noopener,noreferrer');
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl shadow-lg h-full">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold text-white">Sua Rota Otimizada</h2>
        <div className="flex items-center gap-2">
          <button 
            onClick={handleCopy}
            className="flex items-center gap-2 bg-gray-700 hover:bg-gray-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors duration-200"
          >
            <ClipboardIcon className="w-5 h-5" />
            <span>{copied ? 'Copiado!' : 'Copiar Rota'}</span>
          </button>
           <button 
              onClick={handleOpenInMaps}
              className="flex items-center gap-2 bg-blue-600 hover:bg-blue-500 text-white font-semibold py-2 px-4 rounded-lg transition-colors duration-200"
              title="Abrir rota no Google Maps"
            >
              <MapIcon className="w-5 h-5" />
              <span>Abrir no Mapa</span>
            </button>
        </div>
      </div>

      <RouteSummaryCard summary={summary} />

      <div className="space-y-4 relative pr-4 max-h-[500px] overflow-y-auto">
        {/* Vertical line */}
        <div className="absolute left-5 top-5 bottom-5 w-0.5 bg-gray-600"></div>

        {route.map((stop, index) => (
          <div key={index} className="flex items-start gap-4 pl-1">
            <div className="flex-shrink-0 z-10">
              <div className="w-10 h-10 bg-yellow-400 text-gray-900 rounded-full flex items-center justify-center font-bold text-lg shadow-md">
                {stop.order}
              </div>
            </div>
            <div className="flex-grow bg-gray-700/50 p-4 rounded-lg border border-gray-600">
              <div className="flex items-center gap-3 mb-2">
                <MapPinIcon className="w-5 h-5 text-yellow-300 flex-shrink-0"/>
                <p className="font-semibold text-gray-100">{stop.address}</p>
              </div>
              <div className="flex items-center gap-3 text-sm text-gray-400 mb-2">
                 <ClockIcon className="w-5 h-5 flex-shrink-0"/>
                 <span>{stop.estimatedTime}</span>
              </div>
              <p className="text-sm text-gray-300 italic pl-8 border-l-2 border-gray-500 ml-2.5 py-1">
                {stop.justification}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RouteDisplay;