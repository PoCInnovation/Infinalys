const stockNameValidator = {
  stockName: {
    presence: true,
    length: {
      min: 1,
      message: 'stock name is empty',
    },
    format: {
      pattern: /^[A-Z]+(.[A-Z])*$/,
      message: '%{value} is not in a valid format.',
    },
  },
};

module.exports = {
  stockNameValidator,
};
