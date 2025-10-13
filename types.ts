export interface OptimizedStop {
  order: number;
  address: string;
  justification: string;
  estimatedTime: string;
}

export interface RouteSummary {
  totalStops: number;
  totalTime: string;
}

export interface OptimizedRouteResponse {
  route: OptimizedStop[];
  summary: RouteSummary;
}
