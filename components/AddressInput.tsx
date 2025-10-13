import React from 'react';
import { SparklesIcon, TrashIcon, FlagIcon } from './icons';

interface AddressInputProps {
  addresses: string;
  setAddresses: (value: string) => void;
  startPoint: string;
  setStartPoint: (value: string) => void;
  onOptimize: () => void;
  onClear: () => void;
  isLoading: boolean;
}

const AddressInput: React.FC<AddressInputProps> = ({ addresses, setAddresses, startPoint, setStartPoint, onOptimize, onClear, isLoading }) => {
  return (
    <div className="bg-gray-800 p-6 rounded-xl shadow-lg h-full flex flex-col">
      <div>
        <label htmlFor="startPoint" className="block text-lg font-semibold text-gray-100 mb-2">
            Ponto de Partida (Opcional)
        </label>
        <div className="relative">
            <FlagIcon className="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2"/>
            <input
                id="startPoint"
                type="text"
                value={startPoint}
                onChange={(e) => setStartPoint(e.target.value)}
                placeholder="Ex: Endereço do restaurante"
                className="w-full bg-gray-900 text-gray-200 border-2 border-gray-700 rounded-lg p-3 pl-10 focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition duration-200"
                disabled={isLoading}
            />
        </div>
      </div>

      <div className="mt-6 flex flex-col flex-grow">
        <label htmlFor="addresses" className="block text-lg font-semibold text-gray-100 mb-2">
            Endereços para Entrega
        </label>
        <p className="text-sm text-gray-400 mb-4">
            Insira um endereço por linha. Quanto mais endereços, melhor a otimização!
        </p>
        <textarea
            id="addresses"
            value={addresses}
            onChange={(e) => setAddresses(e.target.value)}
            placeholder="Rua das Flores, 123, São Paulo, SP&#10;Avenida Principal, 456, Rio de Janeiro, RJ&#10;Praça Central, 789, Belo Horizonte, MG"
            className="w-full flex-grow bg-gray-900 text-gray-200 border-2 border-gray-700 rounded-lg p-4 focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition duration-200 resize-none"
            rows={10}
            disabled={isLoading}
        />
      </div>

      <div className="mt-6 flex items-stretch gap-4">
        <button
            onClick={onOptimize}
            disabled={isLoading || addresses.trim().length === 0}
            className="flex-grow flex items-center justify-center gap-3 bg-yellow-400 text-gray-900 font-bold py-3 px-6 rounded-lg shadow-md hover:bg-yellow-300 transition-all duration-300 transform hover:scale-105 disabled:bg-gray-600 disabled:cursor-not-allowed disabled:transform-none"
        >
            {isLoading ? (
            <>
                <div className="w-5 h-5 border-2 border-gray-900 border-t-transparent rounded-full animate-spin"></div>
                <span>Otimizando...</span>
            </>
            ) : (
            <>
                <SparklesIcon className="w-6 h-6"/>
                <span>Otimizar Rota</span>
            </>
            )}
        </button>
        <button
            onClick={onClear}
            title="Limpar endereços e rota"
            disabled={isLoading}
            className="flex-shrink-0 bg-red-600 text-white p-3 rounded-lg hover:bg-red-500 transition-colors duration-200 disabled:bg-gray-700 disabled:cursor-not-allowed"
            aria-label="Limpar tudo"
        >
            <TrashIcon className="w-6 h-6" />
        </button>
      </div>
    </div>
  );
};

export default AddressInput;
