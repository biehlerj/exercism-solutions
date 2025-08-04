export const colorCode = (color: string): number => {
  try {
    return COLORS.indexOf(color)
  } catch (error) {
    throw new Error(`Provided color ${color} does not exist.`)
  }
}

export const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white'
]
