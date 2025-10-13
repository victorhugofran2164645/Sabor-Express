
import React from 'react';
import { TruckIcon } from './icons';

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800/50 backdrop-blur-sm p-4 border-b border-gray-700 sticky top-0 z-10">
      <div className="container mx-auto flex items-center gap-4">
        <div className="bg-yellow-400 p-2 rounded-lg">
          <TruckIcon className="w-8 h-8 text-gray-900" />
        </div>
        <div>
            <h1 className="text-3xl font-bold text-white">Sabor Express</h1>
            <p className="text-yellow-400 text-sm">Otimizador de Rotas de Entrega</p>
        </div>
      </div>
    </header>
  );
};

export default Header;
