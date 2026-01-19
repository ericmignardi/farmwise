export interface Farm {
  id: number
  name: string
  location: string
  owner: string
  total_acreage: number
  crop_count: number
  asset_count: number
  created_at: Date
  updated_at: Date
}

export interface Crop {
  id: number
  name: string
  farm: Farm
  planted_date: Date
  harvest_date: Date
  expected_yield: number
  current_value: number
  notes: string
  created_at: Date
}

export interface Asset {
  id: number
  name: string
  asset_type: string
  purchase_date: Date
  purchase_price: number
  current_value: number
  description: string
  created_at: Date
}
