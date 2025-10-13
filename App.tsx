import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import AddressInput from './components/AddressInput';
import RouteDisplay from './components/RouteDisplay';
import LoadingSpinner from './components/LoadingSpinner';
import { OptimizedStop, RouteSummary } from './types';
import { optimizeRoute } from './services/geminiService';
import { TruckIcon } from './components/icons';

const App: React.FC = () => {
  const [addresses, setAddresses] = useState<string>('');
  const [startPoint, setStartPoint] = useState<string>('');
  const [optimizedRoute, setOptimizedRoute] = useState<OptimizedStop[] | null>(null);
  const [routeSummary, setRouteSummary] = useState<RouteSummary | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const LOCAL_STORAGE_KEY = 'saborExpressRouteData';

  // Load saved data on initial render
  useEffect(() => {
    try {
      const savedData = localStorage.getItem(LOCAL_STORAGE_KEY);
      if (savedData) {
        const parsedData = JSON.parse(savedData);
        if (parsedData.optimizedRoute && parsedData.optimizedRoute.length > 0) {
          setOptimizedRoute(parsedData.optimizedRoute);
          setRouteSummary(parsedData.routeSummary);
          setAddresses(parsedData.addresses || '');
          setStartPoint(parsedData.startPoint || '');
        }
      }
    } catch (e) {
      console.error("Failed to load or parse data from localStorage", e);
      localStorage.removeItem(LOCAL_STORAGE_KEY);
    }
  }, []);

  // Save data to localStorage whenever it changes
  useEffect(() => {
    try {
      if (optimizedRoute && optimizedRoute.length > 0 && routeSummary) {
        const dataToSave = {
            optimizedRoute,
            routeSummary,
            addresses,
            startPoint
        };
        localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(dataToSave));
      } else {
        localStorage.removeItem(LOCAL_STORAGE_KEY);
      }
    } catch (e) {
      console.error("Failed to save data to localStorage", e);
    }
  }, [optimizedRoute, routeSummary, addresses, startPoint]);


  const handleOptimize = async () => {
    if (!addresses.trim()) {
      setError('Por favor, insira pelo menos um endereço.');
      return;
    }
    setIsLoading(true);
    setError(null);
    setOptimizedRoute(null);
    setRouteSummary(null);

    try {
      const result = await optimizeRoute(addresses, startPoint);
      setOptimizedRoute(result.route);
      setRouteSummary(result.summary);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Ocorreu um erro desconhecido.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setAddresses('');
    setStartPoint('');
    setOptimizedRoute(null);
    setRouteSummary(null);
    setError(null);
  };

  const WelcomeMessage = () => (
    <div className="flex flex-col items-center justify-center text-center text-gray-400 bg-gray-800 p-6 rounded-xl shadow-lg h-full">
        <TruckIcon className="w-20 h-20 text-gray-600 mb-4"/>
        <h2 className="text-2xl font-bold text-white mb-2">Bem-vindo ao Sabor Express</h2>
        <p>Insira seus endereços de entrega acima e clique em "Otimizar Rota".</p>
        <p className="mt-2 text-sm text-gray-500">Sua rota mais rápida e econômica está a apenas um clique de distância!</p>
    </div>
  );

  const ErrorDisplay = ({ message }: { message: string }) => (
     <div className="flex flex-col items-center justify-center text-center text-red-400 bg-red-900/50 border border-red-500 p-6 rounded-xl shadow-lg h-full">
        <h2 className="text-xl font-bold text-white mb-2">Oops! Algo deu errado.</h2>
        <p>{message}</p>
    </div>
  );


  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Header />
      <main className="container mx-auto p-4 md:p-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div>
            <AddressInput
              addresses={addresses}
              setAddresses={setAddresses}
              startPoint={startPoint}
              setStartPoint={setStartPoint}
              onOptimize={handleOptimize}
              onClear={handleClear}
              isLoading={isLoading}
            />
          </div>
          <div className="min-h-[400px]">
            {isLoading && <div className="flex items-center justify-center h-full"><LoadingSpinner /></div>}
            {error && <ErrorDisplay message={error} />}
            {!isLoading && !error && optimizedRoute && routeSummary && <RouteDisplay route={optimizedRoute} summary={routeSummary} startPoint={startPoint} />}
            {!isLoading && !error && !optimizedRoute && <WelcomeMessage />}
          </div>
        </div>
      </main>
      <footer className="text-center p-4 text-gray-500 text-sm">
        <p>&copy; {new Date().getFullYear()} Sabor Express. Otimizando suas entregas com IA.</p>
      </footer>
    </div>
  );
};

export default App;